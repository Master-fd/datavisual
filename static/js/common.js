


function init_date(chartlist){

    $("#sdate").jeDate({
        isinitVal:true,
        minDate:"1970-01-01",
        format:"YYYY-MM-DD",
        festival: true,
        choosefun: function(elem, date){
            var sdate = $("#sdate").val();
            var edate = $("#edate").val();

            chartlist.forEach(function(value, index, array){
                var dims = value["dims"];
                var item = value["elemid"];
                flushChart(sdate, edate, dims, item);
            });
        }
    })

    $("#edate").jeDate({
        isinitVal:true,
        minDate:"1970-01-01",
        format:"YYYY-MM-DD",
        festival: true,
        choosefun: function(elem, date){
            var sdate = $("#sdate").val();
            var edate = $("#edate").val();

            chartlist.forEach(function(value, index, array){
                var dims = value["dims"];
                var item = value["elemid"];
                flushChart(sdate, edate, dims, item);
            });
        }
    })
}

function flushChart(sdate, edate, dims, elem){

    var url = "/page/getdata";
    var params = {
        sdate : sdate,
        edate : edate,
        dims : dims
    };

    console.log(sdate);
    console.log(edate);
    console.log(dims);
    console.log(elem);
    console.log(url);
    $.getJSON(url, params, function(json_data){

        if (json_data["code"]==0){
            chartSetData(elem, json_data['data'])
        }
    });



}


function chart_init(chartlist){
    //
    chartlist.forEach(function(value, index, array){
        var elem = value['elemid'];
        console.log(elem)
        echarts.init(document.getElementById(elem));
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





