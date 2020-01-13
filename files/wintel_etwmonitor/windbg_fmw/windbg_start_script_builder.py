import os.path
from argparse import ArgumentParser

# Constants
START_SCRIPT = "start_script.txt"
LOOKUP_LOGGER_ID_BY_NAME = "get_diagtrack_listener_logger_id_from_EtwpLookupLoggerIdByName.txt"
LOOKUP_LOGGER_ID_BY_NAME_INTERNAL = "get_diagtrack_listener_logger_id_from_EtwpLookupLoggerIdByName_i.txt"
WRITE_INFO_USER_EVENT = "extract_write_info_from_EtwpWriteUserEvent.txt"
WRITE_INFO_USER_EVENT_INTERNAL = "extract_write_info_from_EtwpWriteUserEvent_i.txt"
WRITE_INFO_WRITE_FULL = "extract_write_info_from_EtwpEventWriteFull.txt"
WRITE_INFO_WRITE_FULL_INTERNAL = "extract_write_info_from_EtwpEventWriteFull_i.txt"
START_DUMP_SERVICES = "print_start_dump_services_db.txt"
PRINT_SERVICE_NAME = "print_service_name_in_db.txt"
END_DUMP_SERVICES = "print_end_dump_services_db.txt"
SC_GENERATE_SERVICE_TAG ="get_name_and_tag_from_ScGenerateServiceTag.txt"

WINDBG_START_SCRIPT_TEMPLATE = """sxd ld
bp nt!pspinsertprocess
g
!gflag +ksl
bc 0 
sxe ld services.exe
g
!gflag -ksl
bp /p @$proc nt!NtMapViewOfSection
g
bp0 /p @$proc ntdll!RtlUserThreadStart
g
ld services
bp0 nt!EtwpLookupLoggerIdByName "$$>a< \\"{scripts_dir}{logger_id_by_name}\\" \\"{two_times_scripts_dir}{logger_id_by_name_i}\\" \\"{three_times_scripts_dir}{write_info_full}\\" \\"{four_times_scipts_dir}{write_info_full_i}\\" \\"{three_times_scripts_dir}{write_info_user}\\" \\"{four_times_scipts_dir}{write_info_user_i}\\""
bp3 services!ScGetServiceNameTagMapping       "$$><\\"{scripts_dir}{start_dump}\\""
bp4 services!ScGetServiceNameTagMapping+0x7d  "$$><\\"{scripts_dir}{print_service}\\""
bp5 services!ScGetServiceNameTagMapping+0x220 "$$><\\"{scripts_dir}{end_dump}\\""
bp6 services!ScGenerateServiceTag+0x3b "$$><\\"{scripts_dir}{generate_service_tag}\\""
gc
"""

def multiple_times_dir(dirpath, times):
    """ 
        Will escape the dir path as times as requested
    """
    multiplied_dirpath = dirpath
    for time in range(times):
        multiplied_dirpath = multiplied_dirpath.replace("\\","\\\\")
    return multiplied_dirpath

def create_start_script(in_dir):
    """
        Will return the string containing all the windbg code for the start script
        Note: Scripts dir must contain the last separatos also!! Example: C:\Windows\\
    """
    return WINDBG_START_SCRIPT_TEMPLATE.format(scripts_dir = multiple_times_dir(in_dir, 1),
                                              two_times_scripts_dir = multiple_times_dir(in_dir, 2),
                                              three_times_scripts_dir = multiple_times_dir(in_dir, 3),
                                              four_times_scipts_dir = multiple_times_dir(in_dir, 4),
                                              logger_id_by_name = LOOKUP_LOGGER_ID_BY_NAME,
                                              logger_id_by_name_i = LOOKUP_LOGGER_ID_BY_NAME_INTERNAL,
                                              write_info_full = WRITE_INFO_WRITE_FULL,
                                              write_info_full_i = WRITE_INFO_WRITE_FULL_INTERNAL,
                                              write_info_user = WRITE_INFO_USER_EVENT,
                                              write_info_user_i = WRITE_INFO_USER_EVENT_INTERNAL,
                                              start_dump = START_DUMP_SERVICES,
                                              print_service = PRINT_SERVICE_NAME,
                                              end_dump = END_DUMP_SERVICES,
                                              generate_service_tag = SC_GENERATE_SERVICE_TAG
                                            )

def write_script(script, out_dir):
    """
        Writes the script to a file
    """
    with open(os.path.join(out_dir, START_SCRIPT),'w') as f:
        f.write(script)
        
                                    
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-d", dest="in_dir", help="Path to directory where all the scripts are")
    parser.add_argument("-o", dest="out_dir", help="Path where the start_script want to be placed")
    args = parser.parse_args()
    if not args.in_dir or not args.out_dir:
        print("Missing parameters")
    
    if args.in_dir[-1] != "\\":
        args.in_dir += "\\"

    script = create_start_script(args.in_dir)
    write_script(script, args.out_dir)