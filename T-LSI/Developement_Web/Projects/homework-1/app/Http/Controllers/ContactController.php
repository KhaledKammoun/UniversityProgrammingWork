<?php

namespace App\Http\Controllers;

use App\Models\Contact;
use Illuminate\Http\Request;

class ContactController extends Controller
{
    function create() {
        return view('atelier1.contact') ;
    }
    public function store(Request $request)
    {
        Contact::create($request->all());
        return view('atelier1.response', ['nom' => $request['nom']]);
    }

}
