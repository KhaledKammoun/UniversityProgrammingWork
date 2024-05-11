<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\TestFormController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/


Route::get('/create', [TestFormController::class, 'create'])->name('createForm');
Route::post('/store', [TestFormController::class, 'store'])->name('storeInfo');









use App\Http\Controllers\TestController;
use App\Http\Controllers\UsersController;
Route::get('/', function () {
    return view('welcome');
});

Route::get('/start', function () {
    return view('start') ;
});


Route::get('/start/{nom}/{age}', [TestController::class, 'index'])->where('nom', '[A-Za-z]+')->where('age', '[0-9]+');

// Forms
Route::get('/users', [UsersController::class, 'create'])->name('create_User') ;
Route::post('/users', [UsersController::class, 'store'])->name('store_User') ;
