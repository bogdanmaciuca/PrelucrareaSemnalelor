"""
Procesarea Semnalelor - Laboratorul 3: Transformata Fourier (Partea I)
Rezolvarea completa a exercitiilor cu explicatii detaliate.
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.animation import FuncAnimation

# Setari generale pentru aspectul graficelor
plt.rcParams['figure.dpi'] = 100
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3


# =============================================================================
# EXERCITIUL 1: Matricea Fourier si verificarea unitaritatii
# =============================================================================
def exercitiul_1():
    print("--- Rulare Exercitiul 1 ---")
    N = 8
    
    # 1.Construim matricea Fourier (N x N)
    # Metoda 1 (explicita, cu doua cicluri for, conform indicatiilor):
    F = np.zeros((N, N), dtype=complex)
    for w in range(N):
        for n in range(N):
            # Folosim math.e si conventia 1j din fizica/Python
            F[w, n] = math.e ** (-2 * math.pi * 1j * w * n / N)
            
    # (Nota: Matriceal s-ar fi putut scrie direct cu produs exterior:
    # k = np.arange(N); F = np.exp(-2j * np.pi * np.outer(k, k) / N))

    # 2. Desenam pe subplot-uri diferite partea reala si imaginara a fiecarei linii
    fig, axes = plt.subplots(N, 2, figsize=(12, 14), sharex=True)
    fig.suptitle(f"Exercițiul 1: Liniile Matricei Fourier pentru N = {N}\n(Stânga: Partea Reală / Cosinus | Dreapta: Partea Imaginară / -Sinus)", fontsize=14)
    
    n_axis = np.arange(N)
    for w in range(N):
        # Coloana 0: Partea Reala (.real)
        axes[w, 0].stem(n_axis, F[w, :].real, linefmt='b-', markerfmt='bo', basefmt='k-')
        axes[w, 0].set_ylabel(f"ω = {w}", fontweight='bold')
        axes[w, 0].set_ylim(-1.3, 1.3)
        if w == 0:
            axes[w, 0].set_title("Partea Reală: Re(F[ω, n])")
            
        # Coloana 1: Partea Imaginara (.imag)
        axes[w, 1].stem(n_axis, F[w, :].imag, linefmt='r-', markerfmt='ro', basefmt='k-')
        axes[w, 1].set_ylim(-1.3, 1.3)
        if w == 0:
            axes[w, 1].set_title("Partea Imaginară: Im(F[ω, n])")

    axes[-1, 0].set_xlabel("Eșantion (n)")
    axes[-1, 1].set_xlabel("Eșantion (n)")
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig("ex1_matricea_fourier.pdf")
    print("Graficul 'ex1_matricea_fourier.pdf' a fost salvat.")

    # 3. Verificam ca matricea F este unitara (pana la factorul N: F^H * F = N * I)
    # Transpusa conjugata (Hermitiana) se obtine cu F.conj().T
    F_hermitian = F.conj().T
    produs = np.dot(F_hermitian, F)
    matrice_asteptata = N * np.eye(N)

    # Verificare cu np.allclose si np.linalg.norm
    este_unitara = np.allclose(produs, matrice_asteptata)
    eroare_norma = np.linalg.norm(produs - matrice_asteptata)

    print(f"Verificare F^H * F == N * I cu np.allclose: {este_unitara}")
    print(f"Norma diferentei ||F^H * F - N*I||: {eroare_norma:.2e}\n")


# =============================================================================
# Functie ajutatoare pentru desenarea unei curbe colorate in functie de raza
# =============================================================================
def plot_colored_complex(ax, z, cmap='viridis'):
    """
    Deseneaza un vector de numere complexe z pe axa 'ax', 
    colorand segmentele in functie de distanta fata de origine (|z|).
    """
    points = np.array([z.real, z.imag]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    distante = np.abs(z)
    
    lc = LineCollection(segments, cmap=cmap, norm=plt.Normalize(0, 1))
    lc.set_array(distante[:-1])
    lc.set_linewidth(2)
    line = ax.add_collection(lc)
    return line


# =============================================================================
# EXERCITIUL 2: Cercul unitate, frecventa de infasurare, culoare + animatie
# =============================================================================
def exercitiul_2(ruleaza_animatii=True):
    print("--- Rulare Exercitiul 2 ---")
    # Alegem o frecventa proprie f = 4 Hz (diferita de 5 Hz din indrumar)
    f_semnal = 4.0  
    N = 1000  # 1000 de esantioane pe durata a 1 secunda (fs = 1000 Hz)
    t = np.linspace(0, 1, N, endpoint=False)
    n_esantioane = np.arange(N)
    
    # Semnalul sinusoidal (folosim cosinus ca in Figura 1 din indrumar, unde x[0]=1)
    x = np.cos(2 * np.pi * f_semnal * t)
    
    # -------------------------------------------------------------------------
    # PARTEA A: Figura 1 (Semnalul in timp si infasurarea cu w = 1 Hz)
    # -------------------------------------------------------------------------
    # y[n] = x[n] * e^(-2*pi*j*t)
    y = x * np.exp(-2j * np.pi * 1 * t)
    idx_marcat = 620  # Esantionul 620 marcat cu rosu, ca in indrumar

    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
    fig1.suptitle(f"Exercițiul 2 (Figura 1): Semnal sinusoidal (f = {f_semnal} Hz) înfășurat pe cercul unitate (ω = 1 Hz)", fontsize=13)

    # Stanga: Semnalul in domeniul timp
    ax1.plot(n_esantioane, x, color='olive', linewidth=1.5)
    ax1.axhline(0, color='black', linewidth=1)
    # Marcam esantionul 620
    ax1.plot([idx_marcat, idx_marcat], [0, x[idx_marcat]], 'r-', linewidth=1.5)
    ax1.plot(idx_marcat, x[idx_marcat], 'ro', markersize=8)
    ax1.set_title("Semnalul în timp x[n]")
    ax1.set_xlabel("Timp (eșantioane)")
    ax1.set_ylabel("Amplitudine")
    ax1.set_xlim(0, N)
    ax1.set_ylim(-1.1, 1.1)

    # Dreapta: Reprezentarea in planul complex colorata dupa distanta de la origine
    line1 = plot_colored_complex(ax2, y, cmap='plasma')
    fig1.colorbar(line1, ax=ax2, label="Distanța de la origine |y[n]|")
    
    ax2.axhline(0, color='black', linewidth=1)
    ax2.axvline(0, color='black', linewidth=1)
    # Marcam corespondenta esantionului 620
    ax2.plot([0, y[idx_marcat].real], [0, y[idx_marcat].imag], 'r-', linewidth=1.5)
    ax2.plot(y[idx_marcat].real, y[idx_marcat].imag, 'ro', markersize=8)
    ax2.set_title("Planul Complex: $y[n] = x[n]e^{-2\\pi j n}$")
    ax2.set_xlabel("Real")
    ax2.set_ylabel("Imaginar")
    ax2.set_xlim(-1.1, 1.1)
    ax2.set_ylim(-1.1, 1.1)
    ax2.set_aspect('equal')

    plt.tight_layout()
    plt.savefig("ex2_figura1_static.pdf")
    print("Graficul 'ex2_figura1_static.pdf' a fost salvat.")

    # -------------------------------------------------------------------------
    # PARTEA B: Figura 2 (Infasurarea pentru 4 frecvente w diferite)
    # -------------------------------------------------------------------------
    # Alegem 4 frecvente, dintre care una este chiar f_semnal = 4 Hz
    frecvente_w = [1, 2, int(f_semnal), 6]
    
    fig2, axes2 = plt.subplots(2, 2, figsize=(10, 10))
    fig2.suptitle(f"Exercițiul 2 (Figura 2): Influența frecvenței de înfășurare ω (f_semnal = {f_semnal} Hz)", fontsize=14)
    axes2 = axes2.flatten()

    for i, w in enumerate(frecvente_w):
        z_w = x * np.exp(-2j * np.pi * w * t)
        # Centrul de greutate (media vectorului z_w = X(w) / N)
        centru_greutate = np.mean(z_w)
        
        ax = axes2[i]
        lc = plot_colored_complex(ax, z_w, cmap='viridis')
        ax.axhline(0, color='black', linewidth=0.8)
        ax.axvline(0, color='black', linewidth=0.8)
        
        # Desenam centrul de masa (ca in Figura 2 din indrumar - punctul negru)
        ax.plot([0, centru_greutate.real], [0, centru_greutate.imag], 'k-', linewidth=2.5)
        ax.plot(centru_greutate.real, centru_greutate.imag, 'ko', markersize=8, label=f"|C| = {np.abs(centru_greutate):.2f}")
        
        ax.set_title(f"$\\omega = {w}$ Hz")
        ax.set_xlabel("Real")
        ax.set_ylabel("Imaginar")
        ax.set_xlim(-1.1, 1.1)
        ax.set_ylim(-1.1, 1.1)
        ax.set_aspect('equal')
        ax.legend(loc="upper right")

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig("ex2_figura2_static.pdf")
    print("Graficul 'ex2_figura2_static.pdf' a fost salvat.\n")

    # -------------------------------------------------------------------------
    # PARTEA C: Versiunea ANIMATA in timp real pentru Figurile 1 si 2
    # -------------------------------------------------------------------------
    if ruleaza_animatii:
        print("Se pregatesc animatiile in timp real (inchide ferestrele grafice pentru a continua)...")
        
        # --- Animatie Figura 1 ---
        fig_anim1, (ax_a1, ax_a2) = plt.subplots(1, 2, figsize=(12, 5.5))
        fig_anim1.suptitle("ANIMAȚIE Figura 1: Desenarea în timp real pe cercul unitate", fontsize=13)
        
        ax_a1.plot(n_esantioane, x, color='lightgray', linewidth=1, label="Semnal complet")
        linie_timp, = ax_a1.plot([], [], color='olive', linewidth=2)
        indicator_timp, = ax_a1.plot([], [], 'ro', markersize=8)
        tija_timp, = ax_a1.plot([], [], 'r-', linewidth=1.2)
        ax_a1.axhline(0, color='black', linewidth=0.8)
        ax_a1.set_xlim(0, N)
        ax_a1.set_ylim(-1.1, 1.1)
        ax_a1.set_xlabel("Timp (eșantioane)")
        ax_a1.set_ylabel("Amplitudine")

        ax_a2.axhline(0, color='black', linewidth=0.8)
        ax_a2.axvline(0, color='black', linewidth=0.8)
        # Folosim scatter pentru a colora fiecare punct in functie de distanta in timp real
        scat_complex = ax_a2.scatter([], [], c=[], cmap='plasma', norm=plt.Normalize(0, 1), s=8)
        indicator_complex, = ax_a2.plot([], [], 'ro', markersize=8)
        raza_complex, = ax_a2.plot([], [], 'r-', linewidth=1.5)
        ax_a2.set_xlim(-1.1, 1.1)
        ax_a2.set_ylim(-1.1, 1.1)
        ax_a2.set_aspect('equal')
        ax_a2.set_xlabel("Real")
        ax_a2.set_ylabel("Imaginar")

        pas = 5  # Desenam cate 5 esantioane pe cadru pentru o viteza fluida
        def update_fig1(frame):
            idx = min(frame * pas, N - 1)
            # Actualizare grafic stanga (Timp)
            linie_timp.set_data(n_esantioane[:idx], x[:idx])
            indicator_timp.set_data([n_esantioane[idx]], [x[idx]])
            tija_timp.set_data([n_esantioane[idx], n_esantioane[idx]], [0, x[idx]])
            
            # Actualizare grafic dreapta (Complex)
            coords = np.column_stack((y[:idx].real, y[:idx].imag))
            scat_complex.set_offsets(coords)
            scat_complex.set_array(np.abs(y[:idx]))
            indicator_complex.set_data([y[idx].real], [y[idx].imag])
            raza_complex.set_data([0, y[idx].real], [0, y[idx].imag])
            return linie_timp, indicator_timp, tija_timp, scat_complex, indicator_complex, raza_complex

        anim1 = FuncAnimation(fig_anim1, update_fig1, frames=N // pas + 1, interval=20, blit=True, repeat=False)

        # --- Animatie Figura 2 ---
        fig_anim2, axes_a2 = plt.subplots(2, 2, figsize=(9, 9))
        fig_anim2.suptitle(f"ANIMAȚIE Figura 2: Înfășurarea în timp real pentru ω ∈ {frecvente_w} Hz", fontsize=13)
        axes_a2 = axes_a2.flatten()
        
        scatters_f2 = []
        indicatori_f2 = []
        raze_f2 = []
        z_list = [x * np.exp(-2j * np.pi * w * t) for w in frecvente_w]

        for i, w in enumerate(frecvente_w):
            ax = axes_a2[i]
            ax.axhline(0, color='black', linewidth=0.8)
            ax.axvline(0, color='black', linewidth=0.8)
            ax.set_xlim(-1.1, 1.1)
            ax.set_ylim(-1.1, 1.1)
            ax.set_aspect('equal')
            ax.set_title(f"$\\omega = {w}$ Hz")
            
            sc = ax.scatter([], [], c=[], cmap='viridis', norm=plt.Normalize(0, 1), s=6)
            ind, = ax.plot([], [], 'ro', markersize=7)
            rz, = ax.plot([], [], 'r-', linewidth=1.2)
            scatters_f2.append(sc)
            indicatori_f2.append(ind)
            raze_f2.append(rz)

        def update_fig2(frame):
            idx = min(frame * pas, N - 1)
            artisti = []
            for i in range(4):
                z_curr = z_list[i]
                coords = np.column_stack((z_curr[:idx].real, z_curr[:idx].imag))
                scatters_f2[i].set_offsets(coords)
                scatters_f2[i].set_array(np.abs(z_curr[:idx]))
                indicatori_f2[i].set_data([z_curr[idx].real], [z_curr[idx].imag])
                raze_f2[i].set_data([0, z_curr[idx].real], [0, z_curr[idx].imag])
                artisti.extend([scatters_f2[i], indicatori_f2[i], raze_f2[i]])
            return artisti

        anim2 = FuncAnimation(fig_anim2, update_fig2, frames=N // pas + 1, interval=20, blit=True, repeat=False)
        
        # Pastram referinta catre animatii pentru a nu fi sterse de Garbage Collector
        plt.show()


# =============================================================================
# EXERCITIUL 3: Transformata Fourier manuala pe un semnal cu 3 componente
# =============================================================================
def exercitiul_3():
    print("--- Rulare Exercitiul 3 ---")
    # Alegem o frecventa de esantionare fs = 500 Hz si N = 500 esantioane (durata = 1s)
    # Conform teoremei Nyquist, putem identifica frecvente pana la fs/2 = 250 Hz.
    N = 500
    fs = 500.0
    t = np.arange(N) / fs  # Vectorul momentelor de timp: n * ts
    
    # Compunem un semnal din 3 frecvente alese de noi:
    f1, A1 = 10.0, 1.5   # Componenta 1: 10 Hz, amplitudine 1.5
    f2, A2 = 35.0, 2.5   # Componenta 2: 35 Hz, amplitudine 2.5
    f3, A3 = 80.0, 0.8   # Componenta 3: 80 Hz, amplitudine 0.8
    
    x = (A1 * np.cos(2 * np.pi * f1 * t) + 
         A2 * np.cos(2 * np.pi * f2 * t) + 
         A3 * np.cos(2 * np.pi * f3 * t))
    
    # Plaja de frecvente de infasurare w pe care o testam: 0 Hz ... 100 Hz
    frecvente_test = np.arange(0, 101, 1)
    num_frecvente = len(frecvente_test)
    
    # -------------------------------------------------------------------------
    # Metoda 1: Calculul DFT cu cicluri repetitive explicite (Relatia 1)
    # -------------------------------------------------------------------------
    X_cicluri = np.zeros(num_frecvente, dtype=complex)
    for idx_w, w in enumerate(frecvente_test):
        suma = 0.0 + 0.0j
        for n in range(N):
            suma += x[n] * (math.e ** (-2 * math.pi * 1j * n * w / N))
        X_cicluri[idx_w] = suma

    # -------------------------------------------------------------------------
    # Metoda 2: Calculul DFT cu Matricea Fourier si produs matrice-vector
    # -------------------------------------------------------------------------
    n_vec = np.arange(N)
    # Construim sub-matricea Fourier de dimensiune (len(frecvente_test) x N)
    F_partial = np.exp(-2j * np.pi * np.outer(frecvente_test, n_vec) / N)
    X_matriceal = np.dot(F_partial, x)
    
    # Verificam ca ambele metode dau exact acelasi rezultat
    assert np.allclose(X_cicluri, X_matriceal), "Eroare: Metodele difera!"
    print("Calculul DFT cu cicluri for si cel matriceal sunt identice (verificat cu np.allclose).")
    
    # Modulul transformatei Fourier |X(w)|
    modul_X = np.abs(X_matriceal)

    # -------------------------------------------------------------------------
    # Afisarea grafica (asemanator Figurii 3 din indrumar)
    # -------------------------------------------------------------------------
    fig3, (ax_timp, ax_frecv) = plt.subplots(1, 2, figsize=(13, 5))
    fig3.suptitle(f"Exercițiul 3 (Figura 3): Identificarea componentelor de frecvență ({f1} Hz, {f2} Hz, {f3} Hz)", fontsize=13)

    # Stanga: Semnalul compus in timp
    ax_timp.plot(t, x, 'b-', linewidth=1)
    ax_timp.set_title("Semnalul compus în domeniul timp $x(t)$")
    ax_timp.set_xlabel("Timp (s)")
    ax_timp.set_ylabel("$x(t)$")
    ax_timp.set_xlim(0, 1)

    # Dreapta: Modulul Transformatei Fourier |X(w)|
    ax_frecv.stem(frecvente_test, modul_X, linefmt='k-', markerfmt='ko', basefmt='k-')
    ax_frecv.set_title("Spectrul de amplitudine $|X(\\omega)|$")
    ax_frecv.set_xlabel("Frecvența (Hz)")
    ax_frecv.set_ylabel("$|X(\\omega)|$")
    ax_frecv.set_xlim(0, 100)
    ax_frecv.set_ylim(0, max(modul_X) * 1.15)
    
    # Adaugam etichete text deasupra varfurilor detectate
    for f_comp in [f1, f2, f3]:
        val_varf = modul_X[int(f_comp)]
        ax_frecv.annotate(f"{int(f_comp)} Hz\n(|X|={val_varf:.0f})",
                          xy=(f_comp, val_varf),
                          xytext=(f_comp, val_varf + 40),
                          ha='center', fontsize=9, fontweight='bold', color='darkred')

    plt.tight_layout()
    plt.savefig("ex3_spectru_fourier.pdf")
    print("Graficul 'ex3_spectru_fourier.pdf' a fost salvat.\n")


if __name__ == "__main__":
    # Rulam toate exercitiile
    exercitiul_1()
    exercitiul_3()
    # Rularea exercitiului 2 la final deoarece contine plt.show() pentru animatii
    exercitiul_2(ruleaza_animatii=True)
