/**********************************************************************
[Portfolio Optimizer] Efficient Frontier
SVG-Custom Scatter Plot

Created On: 09/20/2019              Last Modified: 09/20/2019

**********************************************************************/
console.log("<JavaScript> Import: D3 SVG-ScatterPlot >> Successful")
/*********************************************************************
Set SVG Canvas Dimentions: Height & Width
  - Method 1: Set Using Active Window Size
  - Method 2: Set According to Tag Element Attributes
      - More Reliable Size Reference
*********************************************************************/
// Set SVG Canvas Area Margins
var margin = { top:50, bottom:50, left:50, right:50 };

// Method 1: Active Window Reference
var wndwHeight = window.outerHeight;
var wndwWidth = window.outerWidth;

// Method 2: HTML Tag Element Reference
var svgHeight = parseInt(d3.select("#SVG-Main").style("height"));
var svgWidth = parseInt(d3.select("#SVG-Main").style("width"));

/**********************************************************************
Note: Set Default Height & Width Values Equal to the Size of the Entire
SVG Area Less The Appropriate Margins (Leave Room For Chart Axis).
********************************************************************/
// Set Default Height & Width Parameters
var height = svgHeight - margin.top - margin.bottom;
var width = svgWidth - margin.left - margin.right;

// Define SVG Canvas Area
var svgArea = d3.select("#Efficient-Frontier")
                .append("svg")
                .attr("height", height + margin.top + margin.bottom)
                .attr("height", width + margin.left + margin.right)

/*******************************************************************
Note: The Flow of HTML Webpages is From Top to Bottom. Therefore,
SVG Chart Origin is Located in the Top Left. When Appending HTML
Tag Elements to Build Out the SVG Chart, HTML Tag Elements Must Be
Translated to Their Desired Positions From The Chart Origin.
  - Drawing Chart X and Y Axis
  - Plotting Data Points
********************************************************************/
// Define SVG Chart Area
var chartArea = svg.append("g")
                   .attr(
                      "transform",
                      `translate(${margin.left}, ${margin.top})`
                    )

// Define SVG Chart Axis - Anchor/Start Point
var xAxisGroup = chartArea.append("g")
                          .transition()
                          .duration(1500)
                          .attr("class", "x-axis")
                          .attr(
                            "transform",
                            `translate(0, ${height})`
                          )

// Define SVG Chart Axis - Anchor/Start Point
var yAxisGroup = chartArea.append("g")
                          .transition()
                          .duration(1500)
                          .attr("class", "y-axis")
                          .attr(
                            "transform",
                            `translate(${margin.left}, 0)`
                          )

/***********************************************************************
Define SVG Chart Scaling Functions:

Axis Scaling Functions Will Normalize Any Value to Fall Between the
Min (Domain) and Max (Range)

Define Scale Functions:
  - Min Scale Output: Domain(min, max)
  - Max Scale Output: Range(min, max)

Once Defined, To Draw an Axis Using Scale Function Requires:
  - Start Location
  - Array of Iterable Axis Values

For Dynamic Visualizations Axis Domains Will Change to Reflect the
Data For Which it Describes. However the Range Will Remain Constant
Fixed If Tied Directly to the Height & Width of SVG Canvas. Therefore,
Only Range of Scale Functions Need to Be Defined Here

**Changing The Domain Parameters of Scale Function Will Allow For Dynamic Axis.
Update Function (below)
***************************************************************************/
var xAxisScale = d3.scaleLinear().range([0, width])
var yAxisScale = d3.scaleLinear().range([height, 0])

// Define Dynamic "GetData" Function
function getData(){

  portfolios = []
  // Flask Routes - MySQL Database Functions >> Jsonified Inputs
  d3.json("/FlaskRouteMySQLQuery", function(simulationData){


  })
  updateEfficientFrontier(portfolios)
}




// Define Chart "Update" Function
function updateEfficientFrontier(chartData){

  // Calc Min/Max Values for Axes
  var xMin = d3.min(chartData, function(d){
    return parseInt(d["x"] * .90)
  });
  var xMax = d3.max(chartData, function(d){
    return parseInt(d["x"] * 1.10)
  });
  var yMin = d3.min(chartData, function(d){
    return parseInt(d["y"] * 0.90)
  });
  var yMax = d3.max(chartData, function(d){
    return parseInt(d["y"] * 1.10)
  });

  // Update/Add Domain Values Previously Defined xAxisScale & yAxisScale
  xAxisScale.domain([xMin, xMax])
  yAxisScale.domain([yMin, yMax])

  var xAxis = d3.axisBottom(xScale);
  var yAxis = d3.axisLeft(yScale);


}



