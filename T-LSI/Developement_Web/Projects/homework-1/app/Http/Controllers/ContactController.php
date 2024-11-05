<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ContactController extends Controller
{
    function create() {
        return view('atelier1.contact') ;
    }
    public function store(Request $request)
    {
        $nom = $request['nom'];

        return view('atelier1.response', ['nom' => $nom]);
    }

}
