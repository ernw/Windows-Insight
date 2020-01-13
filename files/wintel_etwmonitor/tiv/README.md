# Windows Telemetry ETW Monitor: Telemetry Information Visualization (TIV) Framework

This folder ("tiv") stores the implementation of the Telemetry Information Visualization (TIV) framework, part of the Windows Telemetry ETW Monitor. The TIV framework is a set of Python scripts that visualize information and statistics based on the data produced by the Windbg Framework (also part of the Windows Telemetry ETW Monitor). 

The output of the TIV framework is a report in the form of a web page.

## Technology domain

The TIV framework is based on Python 3.5.

## Usage guidelines

In order to run the TIV framework, execute the "visualize_data.py" Python script. This script is the central engine of TIV.

The "visualize_data.py" script takes the following parameters: 

- *-i*: specifies the input file. This file is the file to which the Windbg Framework has logged output data;
- *-o*: specifies the output directory. In this directory (which must not exist), TIV stores output files; 
- *--debug* (optional): enables verbose output.

Once the "visualize_data.py" script has finished executing, a new folder is created in the folder specified by the *-o* parameter. The name of the newly created folder is the folder creation timestamp. This folder stores the report displaying information and statistics in the form of a web page (default page: "index.html").

In order to view the report, the content of the newly created folder has to be served by an HTTP server. The simplest way to achieve this is to use the native Python HTTP server. Execute the following command in the newly created folder: 

(Python 2.7)

```bash
python -m SimpleHTTPServer <port>
```

(Python 3.5)

```bash
python -m http.server <port>
```

**Important note**: Opening the "index.html" file directly will fail due to CORS.

### Log output

Log output produced by the TIV framework can be found in the "tiv\log.txt" file.

## Extending the TIV framework

### Adding new statistics

In order to create a new statistic, you must follow these steps:

1. In the "tiv\statistics" folder, create your own object as a subclass of the "Statistic" class 
2. Implement the two functions that are mandatory for statistic objects: *build_statistic* and *get_rendered_format* (take a look at the implementation of the "Statistic" class)
3. Add an import line in the "statisticHelper.py" file (stored in the "tiv\statistics" folder)

### Adding new graphs

In order to create a new graph, you must follow these steps:

1. In the "tiv\graphs" folder, create your own object as a subclass of the "Graph" class
2. Implement the two functions that are mandatory for graph objects: *build_graph_data* and *get_graph_data* (take a look at the implementation of the "Graph" class)
3. Add an import line in the "graphsHelper.py" file (stored in the "tiv\graphs" folder)

## Credits

**Pablo Artuso**
 
⋅⋅⋅ Main contributor

⋅⋅⋅ Email: artusopablo@gmail.com

⋅⋅⋅ Twitter account: [@lmkalg](https://twitter.com/lmkalg)

**Aleksandar Milenkoski** 

⋅⋅⋅ Supervisor and contributor

⋅⋅⋅ Email: amilenkoski@ernw.de

⋅⋅⋅ Twitter account: [@milenkowski](https://twitter.com/milenkowski)

