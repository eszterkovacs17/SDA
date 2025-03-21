---
layout: post
title: "Interactive Plotly Chart"
date: 2025-03-21
categories: data-visualization
---

Below is an interactive Plotly chart:

<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<div id="chart" style="width: 100%; height: 500px;"></div>
<script>
  var data = [{x: [1, 2, 3], y: [10, 20, 30], type: 'scatter'}];
  Plotly.newPlot('chart', data);
</script>

