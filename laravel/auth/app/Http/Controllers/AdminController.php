<?php

// Name space for the controller
namespace App\Http\Controllers;

// Request
use Illuminate\Http\Request;
// Redis
use Illuminate\Support\Facades\Redis;

// Class for handling all the events for the admin
class AdminController extends Controller{

  // Some variables shared
  // stats for top elements
  protected $chartData;
  //stats for consumption
  protected $stateStats;

  // Initilizer
  public function __construct(){
    // Define the states array
    $statesArray = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                       "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                       "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                       "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                       "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"];

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

    // Assign values
    foreach ($statesArray as $key => $state) {

      // Get the data from redis
      $eCnsmptnList = Redis::lrange(strval($state), 0, -1);

      // Calculate the sum for the consumption
      $eCnsmptn = $this->calcSumOfArr($eCnsmptnList);

      // Put it in the array
      // Add to the array
      array_push($stateValues,round($eCnsmptn));
      $this->stateStats[$state] = round($eCnsmptn);
    }

    // Assign values for each state
    $this->chartData = vsprintf($chartDataFormat,$stateValues);
  }

  // Function to show the index page
  public function show(){
    // redis test
    Redis::incr('adminPageViews');

    //make a copy
    $curStats =$this->stateStats;

    // sort the state stats array
    arsort($curStats);

    // return the top 10 elements
    $topStates = array_slice($curStats,0,10);

    // return view with data
    return view('admin')->with("topStates",$topStates);
  }

  // Function to return the chart data for plotting
  public function getChartData(){

    // Return value
    return $this->chartData;
  }

  // Function to calculate the sum for the given array
  public function calcSumOfArr($arr){
    // Variable
    $sum = 0.0;

    // Iterate over array to return sum
    foreach ($arr as $key => $value) {
      $sum += floatval($value);
    }

    //return the sum
    return $sum;
  }
}
