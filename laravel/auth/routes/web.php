<?php
/*
|--------------------------------------------------------------------------
| libraries
|--------------------------------------------------------------------------
*/
use Illuminate\Support\Facades\Redis;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

// Route for welcom page
Route::get('/', function () {
  return view('welcome');
});

// Route for user page
Route::get('user', 'UserController@show');

// Route for admin page
Route::get('admin', function () {
  return view('admin');
});
