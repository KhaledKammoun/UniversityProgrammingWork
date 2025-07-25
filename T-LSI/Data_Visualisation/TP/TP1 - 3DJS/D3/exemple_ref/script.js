// Activité 2 - Application 1
var activite2 = d3
  .select("body")
  .append("div")
  .attr("class", "activite")
  .append("h2")
  .text("Activité 2 - Application 1");

activite2
  .append("h1")
  .text('"C\'est mon premier exemple généré avec D3"')
  .style("color", "black")
  .style("text-align", "center")
  .style("font-style", "italic");

// Activité 3 - Application 1
var activite3 = d3
  .select("body")
  .append("div")
  .attr("class", "activite")
  .append("h2")
  .text("Activité 3 - Application 1");

activite3
  .append("a")
  .attr("href", "https://d3js.org/")
  .attr("target", "blank")
  .text("Visitez le site officiel de D3.js")
  .style("color", "blue")
  .style("font-style", "italic")
  .style("text-decoration", "underline")
  .style("font-size", "18px");

// Activité 3 - Application 2
var activite3_2 = d3
  .select("body")
  .append("div")
  .attr("class", "activite")
  .append("h2")
  .text("Activité 3 - Application 2");

activite3_2
  .append("h1")
  .text('"Image générée avec D3"')
  .style("font-style", "italic")
  .style("color", "red")
  .style("text-align", "center");

activite3_2
  .append("img")
  .attr(
    "src",
    "https://www.powertrafic.fr/wp-content/uploads/2023/04/image-ia-exemple.png"
  )
  .style("display", "block")
  .style("margin", "20px auto")
  .style("width", "300px");

// Activité 4
var activite4 = d3
  .select("body")
  .append("div")
  .attr("class", "activite")
  .append("h2")
  .text("Activité 4");

var svg = activite4
  .append("svg")
  .attr("width", "800px")
  .attr("height", "600px")
  .style("border", "3px solid black");

svg.append("circle").attr("cx", 400).attr("cy", 300).attr("r", 60);

// Application 4
var application4 = d3
  .select("body")
  .append("div")
  .attr("class", "activite")
  .append("h2")
  .text("Application 4");

var svg = application4
  .append("svg")
  .attr("width", "800px")
  .attr("height", "600px")
  .style("border", "3px solid black");

svg
  .append("circle")
  .attr("cx", 400)
  .attr("cy", 300)
  .attr("r", 60)
  .style("fill", "blue")
  .style("stroke", "red")
  .style("strokeWidth", "3px");
