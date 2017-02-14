<?php

// Name space for the controller
namespace App\Http\Controllers;

// Request
use Illuminate\Http\Request;
// Redis
use Illuminate\Support\Facades\Redis;


// Class for handling events with the controller
class UserController extends Controller {

  // Assign a global variable for user id
  protected $user_id;

  // Initilizer to get a random key
  public function __construct(){
    // check if user_id is set
    if(empty($user_id)){
      // get a key for instance
      $this->user_id = Redis::randomkey();
      // tokenize the key
      $this->user_array = explode(":",$tstStr,2);
      // get the user_id from user_array
      $this->user_id=$this->user_array[0];
    }
  }

  // Function to get the data from the redis database
  public function getCnsmptnList($utility="electricity"){
    // Check if it's null
    if(is_null($this->user_id)){
      // Return a zero element array
      return [0];
    }
    // Assign the key
    $thisKey = strval($this->user_id) . ":" . strval($utility);
    // Get the redis list of  the user
    $eCnsmptn = Redis::lrange($thisKey, 0, -1);

    // Return the list of values
    return $eCnsmptn;
  }

  // Function to calculate the sum for the given array
  public function calcSumOfArr($arr){
    // Variable
    $sum = 0.0;

    // Iterate over array to return sum
    foreach ($arr as $key => $value) {
      $sum += floatval($value);
    }

    // Return the value
    return $sum;
  }

  // Function to return the index view
  public function show(){
    // Array of topics
    $topics = array("electricity"=>0.0,"water"=>0.0,"gas"=>0.0);

    // Loop through topics
    foreach ($topics as $key => $topic) {
      $cnsmptnLst = $this->getCnsmptnList(strval($key));
      $cnsmptnSum =  $this->calcSumOfArr($cnsmptnLst);
      $topics[$key]=round($cnsmptnSum,2);
    }

    // Return the view
    return view('user')->with("user_id",$this->user_id)
                       ->with("electricity",$topics["electricity"])
                       ->with("water",$topics["water"])
                       ->with("gas",$topics["gas"]);
  }
}
