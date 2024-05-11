<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div class="container">
        <h1>Informations saisies :</h1>
        <ul>
            <li><strong>Nom:</strong> {{ $nom }}</li>
            <li><strong>Prénom:</strong> {{ $prenom }}</li>
            <li><strong>Âge:</strong> {{ $age }}</li>
            <li><strong>Sexe:</strong> {{ $sexe }}</li>
            <li><strong>Loisirs:</strong>
                <ul>
                    @foreach($loisirs as $loisir)
                        <li>{{ $loisir }}</li>
                    @endforeach
                </ul>
            </li>
        </ul>
    </div>
</body>
</html>