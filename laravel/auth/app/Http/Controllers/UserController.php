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
    if(empty($var)){
      // get a key for instance
      $this->user_id = Redis::randomkey();
    }
  }

  // Function to get the data from the redis database
  public function getElecCnsmptnList(){
    // Get the redis list of  the user
    $eCnsmptn = Redis::lrange($this->user_id, 0, -1);

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
    // Get the array of consumption
    $eCnsmptn = $this->getElecCnsmptnList();

    // Get the sum for consumption
    $eCnsmptnSum = $this->calcSumOfArr($eCnsmptn);
    // Formatting
    $eCnsmptnSum=round($eCnsmptnSum,2);

    // Return the view
    return view('user')->with("user_id",$this->user_id)->with("eCnsmptnSum",$eCnsmptnSum);
  }
}
