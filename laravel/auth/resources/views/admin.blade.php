@extends('layouts.default')

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


@endsection
