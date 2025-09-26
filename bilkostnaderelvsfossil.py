"""
Program: Sammenligning av årlige bilkostnader
Beskrivelse:
Dette programmet regner ut og sammenligner de årlige kostnadene 
ved å eie en elbil kontra en bensinbil. 
Alle tall er basert på oppgitte satser i oppgaveteksten for arbeidskrav 1 i PY-1010.
"""

# -------------------------
# Input: hvor mye du kjører
# -------------------------
kjørelengde_per_år = 10000  # her kan du endre antall km per år

# -------------------------
# Faste kostnader
# -------------------------
trafikkforsikringsavgift_per_dag = 8.38
trafikkforsikringsavgift_per_år = trafikkforsikringsavgift_per_dag * 365

# -------------------------
# Elbil
# -------------------------
forsikring_elbil = 5000
strømforbruk_per_km = 0.2      # kWh per km
strømpris = 2.00               # kr per kWh
bomavgift_elbil_per_km = 0.1   # kr per km

# Beregninger elbil
drivstoff_elbil = kjørelengde_per_år * strømforbruk_per_km * strømpris
bom_elbil = kjørelengde_per_år * bomavgift_elbil_per_km
total_elbil = forsikring_elbil + trafikkforsikringsavgift_per_år + drivstoff_elbil + bom_elbil

# -------------------------
# Bensinbil
# -------------------------
forsikring_bensinbil = 7500
drivstoff_bensinbil_per_km = 1.0
bomavgift_bensinbil_per_km = 0.3

# Beregninger bensinbil
drivstoff_bensinbil = kjørelengde_per_år * drivstoff_bensinbil_per_km
bom_bensinbil = kjørelengde_per_år * bomavgift_bensinbil_per_km
total_bensinbil = forsikring_bensinbil + trafikkforsikringsavgift_per_år + drivstoff_bensinbil + bom_bensinbil

# -------------------------
# Sammenligning
# -------------------------
kostnadsforskjell = total_bensinbil - total_elbil

# -------------------------
# Utskrift av resultat
# -------------------------
print("=================================")
print("   SAMMENLIGNING AV BILKOSTNADER ")
print("=================================")
print(f"Kjørelengde per år: {kjørelengde_per_år} km\n")

print(f"Totalkostnad elbil:     {total_elbil:,.2f} kr per år")
print(f"Totalkostnad bensinbil: {total_bensinbil:,.2f} kr per år\n")

if kostnadsforskjell > 0:
    print(f"Elbil er billigere med {kostnadsforskjell:,.2f} kr per år.")
elif kostnadsforskjell < 0:
    print(f"Bensinbil er billigere med {abs(kostnadsforskjell):,.2f} kr per år.")
else:
    print("Kostnadene er like for begge biltyper.")
