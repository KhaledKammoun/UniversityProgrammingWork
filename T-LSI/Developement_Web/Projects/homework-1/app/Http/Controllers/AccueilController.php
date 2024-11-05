<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class AccueilController extends Controller
{
    //
    function index($nom) {
        return view('atelier1.accueil', compact('nom')) ;
    }

    function create() {
        return view('atelier1.index') ;
    }

    public function store(Request $request)
    {
        $request->validate([
            'nom' => 'required|string',
            'age' => 'required|integer|min:0'
        ]);

        $nom = $request->nom;
        $age = $request->age;

        if ($age >= 18) {
            return view('atelier1.accueil', ['nom' => $nom]);
        } else {
            return view('atelier1.erreur', ['nom' => $nom]) ;
        }
    }

}
