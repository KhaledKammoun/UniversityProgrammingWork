<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\AccueilController;
use App\Http\Controllers\ContactController;

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

Route::get('/', function () {
    return view('app');
})->name('main');

Route::get('/atelier1/{nom}', [AccueilController::class, 'index'])->where('nom', '[a-zA-Z]+')->name('home') ;

Route::get('/info', [AccueilController::class, 'create'])->name('info.create') ;
Route::post('/info', [AccueilController::class, 'store'])->name('info.store');

Route::get("/contact", [ContactController::class, 'create'])->name('contact.create') ;
Route::post('/contact', [ContactController::class, 'store'])->name('contact.store');
