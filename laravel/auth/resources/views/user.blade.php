@extends('layouts.default')

<!-- Heading -->
@section('content')
<div class="headingWrapper">
  <!-- Heading -->
  <div class="container adminHeading">
    <span class="text-center">
      <h2>
        <a href="{{ url('/user') }}">
          Welcome, random user with id: {{$user_id}}!!
        </a>
      </h2>
      <p>This is your portal to view your consumption in realtime</p>
    </span>
  </div>
</div>

<!-- Some stats -->
<div class="container-fluid text-center bg-info">
  <h3>
    Thanks to data pipeline, this page loaded in <b>{{ (microtime(true) - LARAVEL_START) }}s</b>
  </h3>
</div>

<!-- Separation -->
<hr/>


<!-- Dashboard cards -->
<span class="text-center">
  <h3>Your utility consumtion information</h3>
</span>
<div class="container cardsWrapper">
  <div class="row">
    <div class="col-xs-12 col-sm-6 col-md-4">
      <div class="well dashCard green">
        <div class="dashCardHeading">
          <span class="glyphicon glyphicon-tint visible-xs visible-sm smallIcon"></span><label>Water Consumption</label>
        </div>
        <div class="icon hidden-xs hidden-sm">
          <i class="glyphicon glyphicon-tint"></i>
        </div>
        <div class="desc">
          <var>1 gallons</var>
          <label class="text-muted">Water Consumption</label>
        </div>
      </div>
    </div>
    <div class="col-xs-12 col-sm-6 col-md-4">
      <div class="well dashCard green">
        <div class="dashCardHeading">
          <span class="glyphicon glyphicon-flash visible-xs visible-sm smallIcon"></span><label>Electricity Consumption</label>
        </div>
        <div class="icon hidden-xs hidden-sm">
          <i class="glyphicon glyphicon-flash"></i>
        </div>
        <div class="desc">
          <var>{{$eCnsmptnSum}} kWh</var>
          <label class="text-muted">Electricity Consumption</label>
        </div>
      </div>
    </div>
    <div class="col-xs-12 col-sm-6 col-md-4">
      <div class="well dashCard green">
        <div class="dashCardHeading">
          <span class="glyphicon glyphicon-fire visible-xs visible-sm smallIcon"></span><label>Gas Consumption</label>
        </div>
        <div class="icon hidden-xs hidden-sm">
          <i class="glyphicon glyphicon-fire"></i>
        </div>
        <div class="desc">
          <var>1 ccf</var>
          <label class="text-muted">Gas Consumption</label>
        </div>
      </div>
    </div>
</div>
</div>
@endsection
