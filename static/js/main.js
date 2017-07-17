



(function (){

    var chartlist = [
        {
            'elemid' : "chart_1",
            'dims' : 'dsur'
        },
        {
            'elemid' : "chart_2",
            'dims' : 'dsur'
        }
    ];

    init_date(chartlist);
    chart_init(chartlist);

//    chartlist.forEach(function(value, index, array){
//            var dims = value["dims"];
//            var item = value["elemid"];
//            var sdate = $("#sdate").val();
//            var edate = $("#edate").val();
//            flushChart(sdate, edate, dims, item);
//    });

})();