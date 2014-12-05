var width = 1200,
    height = 700;
var cluster = d3.layout.cluster()
    .size([height - 100, width - 160]);
var diagonal = d3.svg.diagonal()
    .projection(function(d) { return [d.x, y(d.y)]; });
var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(500,40)");
var xs = [];   
var ys = [];   
function getXYfromJSONTree(node){           
   xs.push(node.x);          
   ys.push(node.y);           
   if(typeof node.children != 'undefined'){                   
      for ( j in node.children){                           
         getXYfromJSONTree(node.children[j]);                   
      }           
   }   
}   
var ymax = Number.MIN_VALUE;   
var ymin = Number.MAX_VALUE;   
{% load staticfiles %}
d3.json("{% static "dendro.json" %}", function(error, root) {
   getXYfromJSONTree(root);
  var nodes = cluster.nodes(root),
      links = cluster.links(nodes);
   nodes.forEach( function(d,i){                   
      if(typeof xs[i] != 'undefined'){                           
         d.x = xs[i];                   
      }                   
      if(typeof ys[i] != 'undefined'){                           
         d.y = ys[i];                   
      }           
   });           
   nodes.forEach( function(d){                   
      if(d.y > ymax)
         ymax = d.y;
      if(d.y < ymin)                           
         ymin = d.y;           
   });           
   y = d3.scale.linear().domain([ymin, ymax]).range([0, height-200]);           
   yinv = d3.scale.linear().domain([ymax, ymin]).range([0, height-200]);   
  var link = svg.selectAll(".link")
      .data(links)
    .enter().append("path")
      .attr("class", "link")
      .attr("d", diagonal);
  var node = svg.selectAll(".node")
      .data(nodes)
    .enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.x + "," + y(d.y) + ")"; })
  node.append("circle")
      .attr("r", 4.5);
  node.append("text")
      .attr("dx", function(d) { return d.children ? -8 : 8; })
      .attr("dy", 3)
      .style("text-anchor", function(d) { return d.children ? "end" : "start"; })
      .text(function(d) { return d.name; });    
});
d3.select(self.frameElement).style("height", height + "px");