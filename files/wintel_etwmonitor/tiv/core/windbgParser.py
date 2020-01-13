import traceback
from misc.auxiliaries import guid_structure_to_guid_representation
from core.exceptions import ErrorWhenParsing

from misc.logger import logger
from core.date import Date
from core.providerGUID import ProviderGUID
from core.callStack import CallStack
from core.pebInfo import PEBInfo
from core.processInfo import ProcessInfo
from core.eventJsonFormat import EventJsonFormat
from core.eventDescriptor import EventDescriptor
from core.writeInfo import WriteInfo
from core.servicesDatabase import ServicesDatabase
from core.service import Service
from core.serviceTag import ServiceTag
from misc.constants import (DATE_START_PH, DATE_END_PH, WRITE_INFO_END_PH, WRITE_INFO_START_PH, PROVIDER_GUID_START_PH,
                        PROVIDER_GUID_END_PH, CALL_STACK_START_PH, CALL_STACK_END_PH, PROCESS_INFO_START_PH,
                        PROCESS_INFO_END_PH, PEB_INFO_START_PH, PEB_INFO_END_PH, EVENT_DESCRIPTOR_START_PH,
                        EVENT_DESCRIPTOR_END_PH, EVENT_JSON_FORMAT_START_PH, EVENT_JSON_FORMAT_END_PH,
                        SERVICE_TAG_END_PH, SERVICE_TAG_START_PH, SERVICES_DB_DUMP_END, SERVICES_DB_DUMP_START,
                        NEW_SERVICE_ADDED_END, NEW_SERVICE_ADDED_START, LINES_STARTING_INFORMATION)

class WindbgParser:
    
    def __init__(self, debug=False):
        self.debug = debug
        self.writes_info = []
        self.failed_write_info = 0
        self.services_database = ServicesDatabase()
        self.index = 0

    def _get_clean_line(self):
        if self.index < self.total_lines:
            return self.lines[self.index].strip()
        else:
            raise ErrorWhenParsing("Tried to get a line with an index bigger than the total lines")

    def _get_raw_line(self):
        if self.index < self.total_lines -1:
            return self.lines[self.index]
        else:
            raise ErrorWhenParsing("Tried to get a line with an index bigger than the total lines")

    def _parse(self, start_ph=None, end_ph=None, object_to_parse_class=None):
        """
            Skeletor for parsing
        """
        logger.log("Parsing {} at line {}".format(object_to_parse_class.__name__, self.index + 1))

        line = self._get_clean_line()
        if line == start_ph:
            self.index += 1
            object_data = ""
            line = self._get_raw_line()
            while (line.strip() != end_ph) and self.index < self.total_lines - 1:
                if line:
                    object_data += line
                    self.index += 1
                    line = self._get_clean_line()
                    if line in LINES_STARTING_INFORMATION:
                        self.index -= 1 # Hack 
                        raise ErrorWhenParsing("A new starting information object ({}) found at line {} while parsing the current one. Skipping the current one.".format(line ,self.index+2))
                    line = self._get_raw_line()
            if self.index == self.total_lines - 1:
                raise ErrorWhenParsing("{} not found! Entire document was anayzed".format(end_ph))
            _object = object_to_parse_class()
            _object.parse(object_data)
            self.index +=1
        else:
            raise ErrorWhenParsing("Error when parsing {} at line {}. \nLine: \"{}\" ".format(object_to_parse_class.__name__, self.index+1, self.lines[self.index]))
        return _object

    def _parse_service_tag_and_get_service(self):
        """ 
        SERVICE_TAG_START
        <service info>
        SERVICE_TAG_END
        """        
        # This could not be present.
        line = self._get_clean_line()
        if line == SERVICE_TAG_START_PH:
            service_tag =  self._parse( start_ph = SERVICE_TAG_START_PH,
                                        end_ph = SERVICE_TAG_END_PH,
                                        object_to_parse_class= ServiceTag,
                                     )
            service_name = self.services_database.get_service_name_from_tag(service_tag.get_tag())
            return Service(service_name, service_tag)
        else:
            return None
        
    def _parse_date(self):
        """
            DATE_TIMESTAMP_START
            <DATE_LINE>
            DATE_TIMESTAMP_END
        """     
        return self._parse(start_ph= DATE_START_PH,
                    end_ph= DATE_END_PH,
                    object_to_parse_class=Date,
                    )
    
    def _parse_provider_guid(self):
        """
            PROVIDER_GUID_START
            <PROVIDER_DATA>
            PROVIDER_GUID_END
        """
        return self._parse(start_ph= PROVIDER_GUID_START_PH,
                    end_ph= PROVIDER_GUID_END_PH,
                    object_to_parse_class=ProviderGUID,
                    )
    
    def _parse_call_stack(self):
        """
            CALL_STACK_START
            <call_stack_data>
            CALL_STACK_END
        """
        return self._parse(start_ph = CALL_STACK_START_PH,
                           end_ph = CALL_STACK_END_PH,
                           object_to_parse_class = CallStack,
                           )

    def _parse_process_info(self):
        """
            PROCESS_INFO_START
            <process info>
            PROCESS_INFO_END
        """
        return self._parse(start_ph = PROCESS_INFO_START_PH,
                           end_ph = PROCESS_INFO_END_PH,
                           object_to_parse_class = ProcessInfo,
                           )
    
    def _parse_peb_info(self):
        """
            PEB_INFO_START
            <PEB_INFO>
            PEB_INFO_END
        """
        return self._parse( start_ph = PEB_INFO_START_PH,
                            end_ph = PEB_INFO_END_PH,
                            object_to_parse_class = PEBInfo,
                            )

    def _parse_event_descriptor(self):
        """
            EVENT_DESCRIPTOR_START
            <EVENT_DESCRIPTOR_DATA>
            EVENT_DESCRIPTOR_END_PH
        """
        return self._parse(start_ph = EVENT_DESCRIPTOR_START_PH,
                            end_ph = EVENT_DESCRIPTOR_END_PH,
                            object_to_parse_class = EventDescriptor,
                            )

    def _parse_event_in_json_format(self):
        """
            EVENT_JSON_FORMAT_START
            <EVENT_JSON_FORMAT_DATA>
            EVENT_JSON_FORMAT_END
        """
        return self._parse(start_ph = EVENT_JSON_FORMAT_START_PH,
                           end_ph = EVENT_JSON_FORMAT_END_PH,
                           object_to_parse_class = EventJsonFormat,
                           )        

    def _parse_writes_info(self):
        """ 

        """
        line = self._get_clean_line()
        if line == WRITE_INFO_START_PH:
            write_info_offset = str(len(self.writes_info) + self.failed_write_info)
            logger.log(("Beginning to parse Write Info Object number {} at line {}".format(write_info_offset, self.index+1)))
            try:
                self.index += 1
                service = self._parse_service_tag_and_get_service()
                date = self._parse_date()
                provider_guid = self._parse_provider_guid()
                call_stack = self._parse_call_stack()
                process_info = self._parse_process_info()
                peb_info = self._parse_peb_info()
                event_descriptor = self._parse_event_descriptor()
                event_in_json_format = self._parse_event_in_json_format()
                
                write_info = WriteInfo( date = date,
                                        provider_guid = provider_guid,
                                        call_stack = call_stack,
                                        process_info = process_info,
                                        peb_info = peb_info,
                                        event_descriptor = event_descriptor,
                                        event_json_format = event_in_json_format,
                                        service = service,
                                        offset=write_info_offset
                                        )
                self.writes_info.append(write_info)
                if self.debug:
                    print(write_info)
            except ErrorWhenParsing as err:
                logger.warning("Error reading the write info number {}. Probably bad line!".format(write_info_offset))
                self.failed_write_info += 1
                self.index += 1
                raise err
                
        logger.log(("Finished parsing Write Info Object number {}".format(write_info_offset)))

    def _parse_db_dump(self):
        """
            SERVICES_DB_DUMP_START
            <SERVICES_DB_DATA>
            SERVICES_DB_DUMP_END
        """
        self.services_database = self._parse(start_ph = SERVICES_DB_DUMP_START,
                                            end_ph = SERVICES_DB_DUMP_END,
                                            object_to_parse_class = ServicesDatabase
                                            )
    
    def _parse_new_service_to_db(self):
        """
            NEW_SERVICE_ADDED_START
            <service_name>
            NEW_SERVICE_ADDED_END
        """
        service = self._parse(start_ph=NEW_SERVICE_ADDED_START, 
                              end_ph= NEW_SERVICE_ADDED_END,
                              object_to_parse_class=Service
                            )
        self.services_database.add_service(service)

    def _move_index_until_placeholder(self, place_holder):
        line = self._get_clean_line()
        while line != place_holder and self.index < self.total_lines - 1:
            self.index += 1
            line = self._get_clean_line() 
        if line != place_holder and self.index == self.total_lines - 1:
            raise ErrorWhenParsing("While looking to next place holder ({}) the entire document was analyzed.".format(place_holder))

    def _move_index_until_end_of_write(self):
        return self._move_index_until_placeholder(WRITE_INFO_END_PH)

    def _move_index_until_end_of_dump(self):
        return self._move_index_until_placeholder(SERVICES_DB_DUMP_END)
    
    def _move_index_until_end_of_new_service(self):
        return self._move_index_until_placeholder(NEW_SERVICE_ADDED_END)

    def parse(self, file_path):
        
        # Count first the total lines
        # so we don't have to load it in memory 
        # all at once.
        # fd = open(file_path,'r')

        with open(file_path, 'r') as f:
            self.lines = f.readlines()
        
        self.index = 0
        self.total_lines = len(self.lines)
        failed_write_info = 0 
        while self.index < self.total_lines - 1:
            try: 
                line = self._get_clean_line()
                if self.index == 1060:
                    a = 2
                    b = 3

                if line == WRITE_INFO_START_PH:
                    self._parse_writes_info()
                    logger.log("Starting looking for {} at line {}".format(WRITE_INFO_END_PH, self.index))
                    self._move_index_until_end_of_write()
                    logger.log("Found! at line at line {}".format(self.index))
                elif line == SERVICES_DB_DUMP_START:
                    self._parse_db_dump()
                elif line == NEW_SERVICE_ADDED_START: 
                    self._parse_new_service_to_db()
                else:
                    self.index +=1
                    continue
            except ErrorWhenParsing:
                logger.warning("{}".format(traceback.format_exc()))
                continue

        logger.log("Amount of write info parsed: {}".format(str(len(self.writes_info))))
        logger.log("Amount of write info couldn't be parsed: {}".format(str(self.failed_write_info)))

        return self.writes_info[:], self.services_database

