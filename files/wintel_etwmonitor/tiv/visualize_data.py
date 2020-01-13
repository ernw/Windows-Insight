from argparse import ArgumentParser
from core.windbgParser import WindbgParser
from statistics.statisticsHelper import StatisticsHelper
from core.outputHelper import OutputHelper
from graphs.graphsHelper import GraphsHelper
from misc.logger import logger

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-f",
                        dest="filename",
                        help= "Path to file with the output of the windbg scripts."
                        )
    parser.add_argument("-o",
                        dest="output_dir",
                        help="Path where the output will be placed",
                        )
    parser.add_argument("--debug",
                        dest="debug",
                        action="store_true",
                        default=False,
                        help="Activate debug"
                        )
    args = parser.parse_args()
    if not args.filename or not args.output_dir:
        parser.error("Missing either input filename or output dir")

    # Parsing windbg output
    windbg_parser = WindbgParser(debug=args.debug)
    writes_info, services_db = windbg_parser.parse(args.filename)

    # Creating statistics
    sh = StatisticsHelper(writes_info, services_db)
    sh.build_statistics()
    rendered_formats = sh.get_all_rendered_formats()

    # Creating graphs
    gh = GraphsHelper(writes_info)
    gh.build_graphs_data()
    graphs_data = gh.get_all_graphs_data()

    # Creating output
    output_helper = OutputHelper(args.output_dir)
    
    for rendered_format in rendered_formats:
        output_helper.create_html_statistic_report(rendered_format)

    for graph_data in graphs_data:
        output_helper.create_javascript_graph(graph_data)

    output_helper.end_output()
    logger.log_end_msg()
