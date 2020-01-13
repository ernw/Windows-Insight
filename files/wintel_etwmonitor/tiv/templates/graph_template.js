function load{{graph_name}}() {
    var config = {
        type: '{{graph_type}}',
        data: {
            datasets: [{
                data: [
                    {% for value in values %}{{value}},
                    {% endfor %}
                ],
                backgroundColor: [
                    {% for i in range(values|length) %}{{colors[i%(colors|length)]}},
                    {% endfor %}
                ],
                label: '{{graph_label}}'
            }],
            labels: [
                {% for label in labels %}"{{label}}",
                {% endfor %}
            ]
        },
        options: {
            responsive: true,
            legend: {
                display:{{display}}
            },
            title: {
                display: true,
                text: '{{graph_title}}'
            },
            animation: {
                animateScale: true,
                animateRotate: true
            },
            {% if graph_with_time %}
            scales: {
                xAxes: [{
                    type: 'time',
                    distribution: 'series',
                    ticks:{
                        source: 'labels',
                        autoSkip: true,
                        maxTicksLimit: 20
                    },
                    time: {
                        unit: "date",
                        displayFormats: {
                            date: 'MMM d h:mm'
                        }
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Date'
                    }
                }],
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: "{{graph_label}}"
                    },
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
            {% endif %}
        }
    };
    var ctx = document.getElementById('{{graph_name}}').getContext('2d');
    window.my{{graph_name}} = new Chart(ctx, config);
}