<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Html Meta -->
    @include('includes.meta')

    <!-- Scripts for the end head -->
    @include('includes.headscripts')
    @yield('headscripts')
  </head>
  <body>
    <!-- Nav Bar-->
    <div class="clearfix">
      @include('includes.navbar')
    </div>

    <!-- Alerts -->
    <div class="container-fluid">
      @include('includes.alerts')
    </div>

    <!-- Content -->
    <div class="contentWrapper">
      @yield('content')
    </div>

    <!-- Footer -->
    <div class="container-fluid">
      @include('includes.footer')
    </div>

    <!-- Scripts -->
    @include('includes.endscripts')
    @yield('endscripts')
  </body>
</html>
