


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

    var url = "/data/getdata";
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
                data: names
            },
            xAxis: {
                data: xAxis
            },
            yAxis: {},
            series: series
        };

    chart.setOption(option);
}


function checkislogin(){

    if (isLogin==true){
        $("#btn").text('注销');
    }else{
        $("#btn").text('登录');
    }

}


function login(){

    $("#btn").click(function (){

        var elem = $(this);

        if (elem.text()=='登录'){

            var params = {
                account : $("#account").val(),
                password : $("#password").val()
            };
            var url = '/user/login';
            $.post(url, params, function(json_data){

                if (json_data.code==0){
                    elem.text("注销");
                }else{
                    alert(json_data.msg);
                }
            });
        }else{
            var url = '/user/logout';
            $.post(url, {}, function(json_data){

                if (json_data.code==0){
                    elem.text("登录");
                }else{
                    alert(json_data.msg);
                }
            });
        }

    });
}


