<?php

// Name space for the controller
namespace App\Http\Controllers;

// Request
use Illuminate\Http\Request;
// Redis
use Illuminate\Support\Facades\Redis;

// Class for handling all the events for the admin
class AdminController extends Controller{

  // Function to show the index page
  public function show(){
    // redis test
    Redis::incr('adminPageViews');

    // Get the page views
    $adminPageViews = Redis::get('adminPageViews');

    // return view with data
    return view('admin')->with("adminPageViews",$adminPageViews);
  }

  // Function to return the chart data for plotting
  public function getChartData(){

    // Send array type
    // $chartData = [
    //       ['Country', 'Popularity'],
    //       ['US-MA', 200],
    //       ['US-WA', 300],
    //       ['US-PA', 400],
    //       ['US-OR', 500],
    //       ['US-CA', 600],
    //       ['US-WV', 700]
    //     ];

    // Google data frame type
    $chartData =
    '{
      "cols":
          [
            {"id":"","label":"States","pattern":"","type":"string"},
            {"id":"","label":"Consumption","pattern":"","type":"number"}
          ],

      "rows":
          [
            {"c":[{"v":"US-MA","f":null},{"v":200,"f":null}]},
            {"c":[{"v":"US-WA","f":null},{"v":300,"f":null}]},
            {"c":[{"v":"US-PA","f":null},{"v":400,"f":null}]},
            {"c":[{"v":"US-OR","f":null},{"v":500,"f":null}]},
            {"c":[{"v":"US-CA","f":null},{"v":600,"f":null}]},
            {"c":[{"v":"US-WV","f":null},{"v":700,"f":null}]},
          ]
    }';

    // Return value
    return $chartData;
  }
}
