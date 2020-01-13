import os 

# Placeholders 
WRITE_INFO_START_PH = "WRITE_INFO_START";
WRITE_INFO_END_PH = "WRITE_INFO_END";
DATE_START_PH = "DATE_TIMESTAMP_START";
DATE_END_PH = "DATE_TIMESTAMP_END";
PROVIDER_GUID_START_PH = "PROVIDER_GUID_START";
PROVIDER_GUID_END_PH = "PROVIDER_GUID_END";
GROUP_GUID_PH = "GROUP_GUID";
CALL_STACK_START_PH = "CALL_STACK_START";
CALL_STACK_END_PH = "CALL_STACK_END";
GROUP_GUID_NOT_FOUND = "GROUP_GUID_NOT_FOUND";
PROCESS_INFO_START_PH = "PROCESS_INFO_START";
PROCESS_INFO_END_PH = "PROCESS_INFO_END";
PEB_INFO_START_PH = "PEB_INFO_START";
PEB_INFO_END_PH = "PEB_INFO_END";
EVENT_DESCRIPTOR_START_PH = "EVENT_DESCRIPTOR_START";
EVENT_DESCRIPTOR_END_PH = "EVENT_DESCRIPTOR_END";
EVENT_JSON_FORMAT_START_PH = "EVENT_JSON_FORMAT_START";
EVENT_JSON_FORMAT_END_PH = "EVENT_JSON_FORMAT_END";
WRITE_INFO_START_PH = "WRITE_INFO_START";
WRITE_INFO_END_PH = "WRITE_INFO_END"
SERVICE_TAG_START_PH = "SERVICE_TAG_START"
SERVICE_TAG_END_PH = "SERVICE_TAG_END"
SERVICES_DB_DUMP_START = "SERVICES_DB_DUMP_START"
SERVICES_DB_DUMP_END = "SERVICES_DB_DUMP_END"
NEW_SERVICE_ADDED_START = "NEW_SERVICE_ADDED_START"
NEW_SERVICE_ADDED_END = "NEW_SERVICE_ADDED_END"
LINES_STARTING_INFORMATION = [NEW_SERVICE_ADDED_START, SERVICES_DB_DUMP_START, WRITE_INFO_START_PH]

# Call stack
CALL_SITE = "call site";
CALL_STACK_ERROR = "error:"
CALL_STACK_NO_INFO = "0x0"

# Date format
DATE_FORMAT = "%a %b %d %H:%M:%S.%f %Y"

# GENERAL
OPENING_BRACKET = "["
CLOSING_BRACKET = "]"
OPENING_BRACE = "{"
CLOSING_BRACE  = "}"

# Process info
PROCESS = "PROCESS"
CID = "Cid"
PEB = "Peb"
PARENTCID = "ParentCid"
IMAGE = "Image"

# Event Descriptor
ED_ID = "id"
ED_VERSION = "version"
ED_CHANNEL = "channel"
ED_LEVEL = "level"
ED_OPCODE = "opcode"
ED_TASK = "task"
ED_KEYWORD = "keyword"

# Logging
cwd  = os.path.dirname(os.path.realpath(__file__))
LOG_PATH = os.path.join(cwd, '../log.txt')
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
LOGGER_NAME = "logger"

# Event json format
EJF_FOUND_BUFFERS = "found buffers"
EJF_NO_BUFFERS_FOUND = "no buffers found"

# Misc
PEB_NULL = "PEB NULL";
SERIALIZED_FILENAME = "SerializedData.json";
PNG_EXTENSION = ".png";
STATISTICS_OUT_FILEPATH = "statistics.html";

# Statistics General
COUNT = "Count"
PROVIDER_GUID = "Provider GUID"

# Statistics Provide general information
KERNEL_IMAGE = "system"
PROVIDER_GENERAL_INFO_TITLE = "Providers general information"
AMOUNT_OF_WRITES = "Amount of writes"
AMOUNT_OF_USER_WRITES = "Amount of user writes"
AMOUNT_OF_KERNEL_WRITES = "Amount of kernel writes"

# Statistics All Call Stacks
CALL_STACK_INFO_TITLE = "Call stacks information"
CALL_STACK_COLUMN = "Call Stack"
AMOUNT_OF_TIMES_USED = "Amount of times used"
PROVIDERS_THAT_USED_IT = "Providers that used it"
ID = "ID"

# Statistics event id per provider
EVENT_ID_PROVIDER_TITLE = "Event ID per Provider"
EVENT_ID = "Event ID"
AMOUNT_OF_EVENTS = "Amount of events"


# Statisics All events written 
ALL_EVENTS_WRITTEN_TITLE = "All events written"
EVENT_CHANNEL = "Channel"
EVENT_TYPE = "Type"
EVENT_VERSION  = "Version"
EVENT_LEVEL = "Level"
EVENT_OPCODE = "Opcode"
EVENT_TASK = "Task"
EVENT_KEYWORD = "Keyword"
EVENT_DATE = "Date"
EVENT_SENDER = "Sender"
EVENT_MSG = "Message"


# Statistics Services DB
SERVICE_NAME = "Service Name"
SERVICE_TAG = "Service Tag"

# Writes per Minute Graph
WPM_DATE_FORMAT = "%m/%d/%y %H:%M"
WPM_NAME = "WritesPerMinute"
WPM_FILENAME = "writes_per_minute"
WPM_TYPE = "bar"
WPM_LABEL = "Amount of writes"
WPM_TITLE = "Writes per Minute"
WPM_DISPLAY_LEGEND = "false"
WPM_GRAPH_WITH_TIME = True

# Calls per process graph
CPP_NAME = "CallsPerProcess"
CPP_TYPE = "doughnut"
CPP_LABEL = "Calls"
CPP_TITLE = "Calls per Process"
CPP_FILENAME = "calls_per_process"
CPP_DISPLAY_LEGEND = "true"
CPP_GRAPH_WITH_TIME = False


# SVCHOST graph
SVCHOST_PROCESS_NAME = "svchost.exe"
SVC_NAME = "SVCHostCalls"
SVC_TYPE = "doughnut"
SVC_LABEL = "Amount of calls"
SVC_TITLE = "SVCHost calls by service"
SVC_FILENAME = "calls_by_services_svchost"
SVC_DISPLAY_LEGEND = "true"
SVC_GRAPH_WITH_TIME = False

# Output
OUTPUT_DATETIME_FMT = "%d_%m_%y_%H_%M_%S"
REPORTS_DIR_NAME = "reports"
WRITE_MODE = "w"
READ_MODE = "r"
GRAPHS_DIR_NAME = "graphs"
TEMPLATES_DIR_NAME = "../templates"

# HTML 
current_wd = os.path.dirname(os.path.realpath(__file__))
HTML_STATISTIC_REPORT_TEMPLATE_NAME = "statistic_template.html"
HTML_STATISTIC_REPORT_TEMPLATE_PATH = os.path.join(current_wd, TEMPLATES_DIR_NAME, HTML_STATISTIC_REPORT_TEMPLATE_NAME)
HTML_INDEX_NAME = "index.html"
HTML_INDEX_TEMPLATE_NAME = "index_template.html"
HTML_INDEX_TEMPLATE_PATH = os.path.join(current_wd, TEMPLATES_DIR_NAME, HTML_INDEX_TEMPLATE_NAME)
HTML_STYLE_PAGE_NAME = "styles.css"
HTML_STYLE_PAGE_PATH = os.path.join(current_wd, TEMPLATES_DIR_NAME, HTML_STYLE_PAGE_NAME)
HTML_EXTENSION = ".html"
HTML_GRAPH_REPORT_TEMPLATE_NAME = "graph_report_template.html" 
HTML_GRAPH_REPORT_TEMPLATE_PATH = os.path.join(current_wd,TEMPLATES_DIR_NAME, HTML_GRAPH_REPORT_TEMPLATE_NAME)

# JS
JS_GRAPH_TEMPLATE_NAME = "graph_template.js"
JS_GRAPH_TEMPLATE_PATH = os.path.join(current_wd, TEMPLATES_DIR_NAME, JS_GRAPH_TEMPLATE_NAME)
JS_EXTENSION = ".js"
JS_DIRECTORY_NAME = "js"
JS_DIRECTORY_PATH = os.path.join(current_wd, TEMPLATES_DIR_NAME, JS_DIRECTORY_NAME)
JS_COLORS = ["window.chartColors.red","window.chartColors.orange","window.chartColors.yellow","window.chartColors.green","window.chartColors.blue",]

