<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form method="POST" action="{{ route('storeInfo') }}">
        @csrf
        <div>
            <label for="nom">Nom:</label>
            <input type="text" id="nom" name="nom">
        </div>
        <div>
            <label for="prenom">Prénom:</label>
            <input type="text" id="prenom" name="prenom">
        </div>
        <div>
            <label for="age">Âge:</label>
            <input type="text" id="age" name="age">
        </div>
        <div>
            <label for="sexe">Sexe:</label>
            <select class="form-control" id="sexe" name="sexe">
                <option value="homme">Homme</option>
                <option value="femme">Femme</option>
            </select>
        </div>
        <div>
            <label for="loisirs">Loisirs:</label><br>
            <input type="checkbox" id="football" name="loisirs[]" value="football">
            <label for="football">Football</label><br>
            <input type="checkbox" id="lecture" name="loisirs[]" value="lecture">
            <label for="lecture">Lecture</label><br>

            <input type="checkbox" id="lecture" name="loisirs[]" value="Jeux Video">
            <label for="jeux_video">Jeux Video</label><br>
        </div>
        <button type="submit" class="btn btn-primary">Envoyer</button>
    </form>
</body>
</html>