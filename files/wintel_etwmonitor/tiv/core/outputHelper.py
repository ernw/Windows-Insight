import os
import shutil

from datetime import datetime
from jinja2 import Template
from misc.constants import (HTML_STATISTIC_REPORT_TEMPLATE_PATH, 
                       OUTPUT_DATETIME_FMT, REPORTS_DIR_NAME, WRITE_MODE,
                       HTML_INDEX_TEMPLATE_PATH, HTML_STYLE_PAGE_PATH,
                       HTML_STYLE_PAGE_NAME, READ_MODE, HTML_INDEX_NAME,
                       HTML_EXTENSION, GRAPHS_DIR_NAME, JS_DIRECTORY_PATH,
                       JS_GRAPH_TEMPLATE_PATH, JS_EXTENSION, JS_DIRECTORY_NAME,
                       HTML_GRAPH_REPORT_TEMPLATE_PATH, JS_COLORS)
from misc.logger import logger

class OutputHelper:

    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.output_dir_for_this_run = ""
        self.statistics_reports_created = []
        self.graphs_created = []
        self._create_output_directory_if_not_exist()
        self._create_output_directory_for_this_run()
        self._copy_fixed_files_to_output_directory()
        self._create_reports_directory()
        self._create_graphs_directory()
    
    def _report_title_to_filename(self, title):
        return title.replace(" ", "_").lower()

    def _create_dir(self, _dir):
        try:
            os.mkdir(_dir)
        except OSError:
            logger.error("Coulndn't create directory for output {}".format(_dir))
            logger.error("{}".format(traceback.format_exc()))
            print("Couldn't create the directory {} for output. Please contact ERNW's team.".format(_dir))

    def _create_output_directory_if_not_exist(self):
        """ 
            Creates the general output directory
        """

        if not os.path.isdir(self.output_dir):
            self._create_dir(self.output_dir)
           
    def _create_output_directory_for_this_run(self):
        """
            Creates the output directory for this run
        """
        directory_name = datetime.now().strftime(OUTPUT_DATETIME_FMT)
        self.output_dir_for_this_run = os.path.join(self.output_dir, directory_name)
        self._create_dir(self.output_dir_for_this_run)

    def _copy_fixed_files_to_output_directory(self):
        """ 
            Copies the css file and js directory 
            to the output directory for this run
        """
        src = HTML_STYLE_PAGE_PATH
        dst = os.path.join(self.output_dir_for_this_run, HTML_STYLE_PAGE_NAME)
        shutil.copy(src, dst)

        src = JS_DIRECTORY_PATH
        dst = os.path.join(self.output_dir_for_this_run, JS_DIRECTORY_NAME)
        shutil.copytree(src,dst)

    def _create_reports_directory(self):
        """
            Creates the reports directory inside the 
            directory for the current run
        """
        self.reports_dir = os.path.join(self.output_dir_for_this_run, REPORTS_DIR_NAME)
        self._create_dir(self.reports_dir)

    def _create_graphs_directory(self):
        """
            Create the graphs directory inside the
            directory for this run
        """
        self.graphs_dir = os.path.join(self.output_dir_for_this_run, GRAPHS_DIR_NAME)
        self._create_dir(self.graphs_dir)

    def create_html_statistic_report(self, rendered_format):
        """
            Creates the HTML statistic report for the object
            provided by params using the HTML template for reports.
        """
        html_statistic_report_template = open(HTML_STATISTIC_REPORT_TEMPLATE_PATH, READ_MODE).read()
        jinja_template = Template(html_statistic_report_template)
        report_title = rendered_format.get_title()
        html_report = jinja_template.render( title= report_title,
                                           columns= rendered_format.get_columns(),
                                           rows = rendered_format.get_rows()
        )   
        report_filename = self._report_title_to_filename(report_title)
        report_path = os.path.join(self.reports_dir, report_filename + HTML_EXTENSION)
        with open(report_path, WRITE_MODE) as f:
            f.write(html_report)
        
        
        self.statistics_reports_created.append((report_title, report_filename))
        
    def _create_javascript_graph(self, graph_data):
        """
            Creates the js file for the graph using
            the template
        """
        js_graph_template = open(JS_GRAPH_TEMPLATE_PATH, READ_MODE).read()
        jinja_template = Template(js_graph_template)
        graph_path = os.path.join(self.graphs_dir, graph_data.get_filename())
        graph = jinja_template.render(graph_name= graph_data.get_name(),
                                      graph_type= graph_data.get_type(),
                                      graph_label= graph_data.get_label(),
                                      graph_title= graph_data.get_title(),
                                      values= graph_data.get_values(),
                                      labels= graph_data.get_labels(),
                                      graph_filename=graph_path,
                                      colors = JS_COLORS,
                                      display= graph_data.get_display_legend(),
                                      graph_with_time = graph_data.get_with_time()
                                      )

        with open(graph_path, WRITE_MODE) as f:
            f.write(graph)

        self.graphs_created.append(graph_data)

    def _create_graph_report(self, graph_data):
        """
            In order to print out the JS graph we
            need to have an html to devide the div.
        """
        import os
        current_wd = os.path.dirname(os.path.realpath(__file__))
        html_graph_report_template = open(HTML_GRAPH_REPORT_TEMPLATE_PATH, READ_MODE).read()
        jinja_template = Template(html_graph_report_template)
        graph_report = jinja_template.render(graph_id =  graph_data.get_id())
        graph_report_path = os.path.join(self.reports_dir, graph_data.get_filename() + HTML_EXTENSION)
        with open(graph_report_path,WRITE_MODE) as f:
            f.write(graph_report)

        self.statistics_reports_created.append((graph_data.get_title(), graph_data.get_filename()))

    def create_javascript_graph(self, graph_data):
        """
            Creates the js file for the graph inside the 
            dir on graphs, and update the index.html 
            with the path and more to this graph
        """
        self._create_javascript_graph(graph_data)
        self._create_graph_report(graph_data)
    
    def _graph_data_format_to_index_format(self, graphs_data):
        """ 
            Workaround to work with jinja2 templating
        """
        graphs_data_new_format = []
        for graph_data in graphs_data:
            name  = graph_data.get_name()
            _id  = graph_data.get_id()
            filename = graph_data.get_filename()
            graphs_data_new_format.append((name, _id, filename))
        return graphs_data_new_format

    def end_output(self):
        """
            This function is intended to update the index
            with all the new reports and charts data.
        """
        html_index_template = open(HTML_INDEX_TEMPLATE_PATH, READ_MODE).read()
        jinja_template = Template(html_index_template)
        graphs_data = self._graph_data_format_to_index_format(self.graphs_created) 
        html_index = jinja_template.render(reports = self.statistics_reports_created,
                                           graphs_data = graphs_data
        )
        index_path = os.path.join(self.output_dir_for_this_run, HTML_INDEX_NAME)
        with open(index_path, WRITE_MODE) as f:
            f.write(html_index)