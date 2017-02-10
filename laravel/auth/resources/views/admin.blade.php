@extends('layouts.default')
<!-- Header scripts-->
@section('headscripts')
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<script type="text/javascript">

  // Define the visualization
  google.charts.load('upcoming', {'packages':['geochart']});

  // Callback to execute
  google.charts.setOnLoadCallback(drawChart);

  // Do the call back
  function drawChart() {
    var jsonData = $.ajax({
      url: "getChartData",
      dataType: "json",
      async: false
      }).responseText;

      var data = new google.visualization.DataTable(jsonData);

      var options = {
        colorAxis: {colors: ['#EEE','#3097d1','#003366']},
        backgroundColor: { fill:'transparent' },
        datalessRegionColor: '#A9A9A9',
        defaultColor: '#EEE',
        region: "US",
        resolution: "provinces",
      };

      var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

      chart.draw(data, options);
    }
</script>

<!-- <script type="text/javascript">

  // Load the Visualization API and the piechart package.
  google.charts.load('current', {'packages':['corechart']});

  // Set a callback to run when the Google Visualization API is loaded.
  google.charts.setOnLoadCallback(drawChart);

  function drawChart() {
    var jsonData = $.ajax({
      url: "getChartData",
      dataType: "json",
      async: false
      }).responseText;

      // Create our data table out of JSON data loaded from server.
      var data = new google.visualization.DataTable(jsonData);
      alert(jsonData);

      // Instantiate and draw our chart, passing in some options.
      var pieChart = new google.visualization.PieChart(document.getElementById('chart_div'));
      pieChart.draw(data, {width: 400, height: 240});
}
</script> -->
@endsection

<!-- Heading -->
@section('content')
<div class="headingWrapper">
  <!-- Heading -->
  <div class="container adminHeading">
    <span class="text-center">
      <h2><a href="{{ url('/admin') }}">Welcome Captain!!</a></h2>
      <p>An admin dashboard for overall statistics.</p>
    </span>
  </div>
</div>

<!-- Separation -->
<hr/>

<!-- Dashboard cards -->
<div class="container-fluid chartWrapper">
  <div class="col-xs-12 col-sm-6 col-md-6">
    <div class="row">
      <span class="text-center">
        <h3>Interactive Map of Consumption</h3>
      </span>
      <hr />
      <div id="regions_div" class="chartArea"></div>
    </div>
  </div>
  <div class="col-xs-12 col-sm-6 col-md-6">
    <div class="row">
      <span class="text-center">
        <h3>Top 10 cities with highest consumption</h3>
      </span>
      <hr />
      <div id="chart_div"></div>
    </div>
  </div>
</div>
@endsection
