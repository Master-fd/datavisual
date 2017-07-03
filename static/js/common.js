



function init_date(date_id, func){

    $("#"+date_id).jeDate({
        isinitVal:true,
        minDate:"1900-01-01",
        format:"YYYY-MM-DD",
        festival: true,
        choosefun: function(elem,date){
            var sdate = $("#sdate").val();
            var edate = $("#edate").val();
            func(sdate, edate);
        }
    })

    return $("#"+date_id).val()
}




function chart_init(elem){
    //
    var myChart = echarts.init(document.getElementById(elem));

}


function get_data(sdate, edate, dims, elem){

    var url = "127.0.0.1:8000/getdata/";
    var params = {
        sdate : sdate,
        edate : edate,
        dims : dims
    };

    $.get(url, params, function(json_data){

        if (json_data["code"]==0){
            chartSetData(elem, json_data['data'])
        }
    });

}

function chartSetData(elem, data){


    var title=data["title"];
    var series=data["series"];
    var xAxis=data["xAxis"];
    var names = [];
    series.forEach(function(value, index, array){

        names.push(value["name"]);
    })

    var chart = echarts.getInstanceByDom(document.getElementById(elem));

    var option = {
            title: {
                text: title
            },
            tooltip: {},
            legend: {
                data: names //['销量']
            },
            xAxis: {
                data: xAxis //["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
            },
            yAxis: {},
            series: series
        };

    chart.setOption(option);
}


function flushChart(elem){

    var dims = '1atr'
    var sdate = $("#sdate").val();
    var edate = $("#edate").val();


    get_data(sdate, edate, dims, elem)
}





