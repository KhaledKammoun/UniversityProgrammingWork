<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homework 1.0</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    
</head>
<body class="bg-light text-dark">

    <!-- Navbar -->
  <div class="navbar-wrapper ">
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid d-flex justify-content-center">
        <a class="navbar-brand" href="/">Homework 1.0</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class=" collapse navbar-collapse justify-content-center" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="/">Home</a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="/Atelier" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Atelier 1
                </a>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="{{route('home', ['nom' => "Khaled"])}}">Exercice 1</a></li>
                  <li><a class="dropdown-item" href="{{route('info.create')}}">Exercice 2</a></li>
                </ul>
              </li> 
   
            <li class="nav-item">
              <a class="nav-link" href="{{route('contact.create')}}">Contact</a>
            </li>
            
          </ul>
        </div>
        <a href="https://github.com/KhaledKammoun" target="_blank" class=" d-flex align-items-center text-decoration-none text-dark" style="gap: 10px; font-weight: 600; font-size: 1.1em;">
          <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/>
          </svg>
          <span>Khaled Kammoun</span>
      </a>
      
      <style>
          a:hover .bi-github {
              color: #333;
              transform: scale(1.1);
          }
          a:hover span {
              color: #333;
              text-decoration: underline;
          }
      </style>
      
      </div>
    </nav>
  </div>
    <section class="text-center py-2 font-bold h-100" >
        <div class="bg-dark bg-opacity-80 py-5 px-3 rounded mx-2" style="background-image: url('https://images.prismic.io/chriswillerton/b1fc65cd-752d-4a5f-86a6-a365c316f3bf_testing-laravel-socialite.png?auto=compress,format'); background-size: cover; background-position: center; min-height: 30vh;">
            <h1 class="display-4 text-white mb-3">Bienvenue sur Homework 1.0</h1>
            <p class="lead text-light mb-4">Explorez les exercices et contactez-nous pour plus d'informations.</p>
            <a href="#main-section" class="btn btn-primary">Voir l'Atelier 1</a>
        </div>
    </section>

<!-- Main Section -->
<section class="container py-5" id="main-section">
  <h2 class="text-center mb-5 display-4 font-weight-bold text-primary">Atelier 1</h2>
  <div class="row g-4">
      <div class="col-lg-4 col-md-6">
          <div class="card shadow border-0 rounded-lg" style="height: 100%;">
              <div class="card-body p-4 ">
                  <h5 class="card-title fs-3 text-secondary">Exercice 1</h5>
                  <p class="card-text">Faites l'exercice 1 pour comprendre comment fonctionnent les routes.</p>
                  <a href="{{route('home', ['nom' => "Khaled"])}}" class="btn btn-primary mt-3">Voir l'exercice</a>
              </div>
          </div>
      </div>

      <div class="col-lg-4 col-md-6">
          <div class="card shadow border-0 rounded-lg h-100">
              <div class="card-body p-4">
                  <h5 class="card-title fs-3 text-secondary">Exercice 2</h5>
                  <p class="card-text">Saisissez vos informations : votre nom et votre âge. En fonction du nom que vous avez donné, nous vous dirons si vous êtes mineur ou majeur. Faites l'exercice 2.</p>
                  <a href="{{route('info.create')}}" class="btn btn-primary mt-3">Voir l'exercice</a>
              </div>
          </div>
      </div>

      <div class="col-lg-4 col-md-6">
          <div class="card shadow border-0 rounded-lg h-100">
              <div class="card-body p-4 text-center">
                  <h5 class="card-title fs-3 text-secondary">Contactez-nous</h5>
                  <a href="{{route('contact.create')}}" class="btn btn-outline-primary mt-3">Contactez-nous</a>
              </div>
          </div>
      </div>
  </div>
</section>


    <!-- Footer -->
    <footer class="bg-body-tertiary text-center text-lg-start">
      <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.05);">
        © 2024 Copyright:
        <a class="text-body" href="{{route('main')}}">Homework 1.0</a>
      </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
