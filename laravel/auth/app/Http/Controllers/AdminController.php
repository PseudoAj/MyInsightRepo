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
}
