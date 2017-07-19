



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

    checkislogin();
    login();

})();