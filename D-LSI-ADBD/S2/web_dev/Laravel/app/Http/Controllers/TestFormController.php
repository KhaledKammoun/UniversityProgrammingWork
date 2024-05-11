<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class TestFormController extends Controller
{
    //
    public function create() {
        return view("info") ;
    }
    public function store(Request $request) {
        $nom = $request->input('nom');
        $prenom = $request->input('prenom');
        $age = $request->input('age');
        $sexe = $request->input('sexe');
        $loisirs = $request->input('loisirs');

        return view('afficheInfo', compact('nom', 'prenom', 'age', 'sexe', 'loisirs'));
    }
}
