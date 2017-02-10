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

    // Define a format for the data
    $chartDataFormat =
    '{
      "cols":
          [
            {"id":"","label":"States","pattern":"","type":"string"},
            {"id":"","label":"Consumption","pattern":"","type":"number"}
          ],

      "rows":
          [
            {"c":[{"v":"US-AL","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-AK","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-AZ","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-AR","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-CA","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-CO","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-CT","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-DC","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-DE","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-FL","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-GA","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-HI","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-ID","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-IL","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-IN","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-IA","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-KS","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-KY","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-LA","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-ME","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-MD","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-MA","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-MI","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-MN","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-MS","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-MO","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-MT","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-NE","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-NV","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-NH","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-NJ","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-NM","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-NY","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-NC","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-ND","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-OH","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-OK","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-OR","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-PA","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-RI","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-SC","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-SD","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-TN","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-TX","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-UT","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-VT","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-VA","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-WA","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-WV","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-WI","f":null},{"v":%d,"f":null}]},
            {"c":[{"v":"US-WY","f":null},{"v":%d,"f":null}]},
          ]
    }';

    // Array of values
    $stateValues = [];
    // Assign random values
    for($i=0;$i<51;$i++){
      // generate random value
      $thisVal = rand(200,1000);

      // Add to the array
      array_push($stateValues,$thisVal);
    }

    // Assign values for each state
    $chartData = vsprintf($chartDataFormat,$stateValues);


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
    // $chartData =
    // '{
    //   "cols":
    //       [
    //         {"id":"","label":"States","pattern":"","type":"string"},
    //         {"id":"","label":"Consumption","pattern":"","type":"number"}
    //       ],
    //
    //   "rows":
    //       [
    //         {"c":[{"v":"US-MA","f":null},{"v":200,"f":null}]},
    //         {"c":[{"v":"US-WA","f":null},{"v":300,"f":null}]},
    //         {"c":[{"v":"US-PA","f":null},{"v":400,"f":null}]},
    //         {"c":[{"v":"US-OR","f":null},{"v":500,"f":null}]},
    //         {"c":[{"v":"US-CA","f":null},{"v":600,"f":null}]},
    //         {"c":[{"v":"US-WV","f":null},{"v":700,"f":null}]},
    //       ]
    // }';

    // Return value
    return $chartData;
  }
}
