<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Welcome Page</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #f8f9fa; 
        }
        .welcome-section {
            background-color: white; 
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body class="bg-light text-dark d-flex align-items-center" style="min-height: 100vh;">

    <section class="container h-100">
        <div class="welcome-section text-center">
            <h2 class="text-lg font-bold mb-4">Congratulations, {{$nom}}</h2>
            <p class="lead">Votre message a été envoyé avec success.</p>
            <a href="/" class="btn btn-primary mt-3">Go to Home</a>
        </div>
    </section>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
