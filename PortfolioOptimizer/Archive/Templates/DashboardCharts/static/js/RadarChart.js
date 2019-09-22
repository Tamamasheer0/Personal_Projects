console.log("<JavaScript> Chart.js - RadarChart")

var color = Chart.helpers.color;                        // Library: Chart Color Refs
var htmlTag = document.getElementById("chart-radar");   // HTML Tag: Radar Chart Canvas
var configRadar = {
    type:"radar",
    data:{
        labels:[
            ["Sharpe", "Ratio"],
            ["Portfolio", "Return"],
            ["Portfolio", "Variance"],
            ["Portfolio", "Beta"],
            ["5-Year", "Performance"]
        ],
        datasets:[{
            // Test Data - User Portfolio Performance Metrics
            label:"Portfolio",
            backgroundColor:color("red").alpha(0.2).rgbString(),
            pointBackgroundColor:"red",
            lineTension:0,
            data: [.825, .182, .127, 1.225, .165]
        },{
            // Test Data - S&P 500 Performance Metrics
            label:"S&P 500",
            backgroundColor:color("blue").alpha(0.2).rbgString(),
            pointBackgroundColor:"blue",
            lineTension:0,
            data:[.623, .231, .111, .871, .123]
        }],
        options:{
            legend:{position:"top"},
            title:{
                display:true,
                text:"Portfolio Metrics",
                scale:{
                    ticks:{
                        beginAtZero:false
                    } // ticks
                } // scale
            }, // title
        } // options
    } // data
} // configRadar

window.onload = function(){
    console.log(htmlTag)
    console.log(configRadar)
    window.myRadar = new Chart(htmlTag, configRadar)
}
