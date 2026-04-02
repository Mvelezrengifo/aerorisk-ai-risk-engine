import csv
from global_route_study import run_global_route_study

def export_routes():
    results = run_global_route_study()
    with open("route_risk_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "origin", "destination", "segments", "avg_risk", "max_risk"
        ])
        for r in results:
            writer.writerow([
                r["origin"], r["destination"], r["segments"], r["avg_risk"], r["max_risk"]
            ])

if __name__ == "__main__":
    export_routes()
    print("route_risk_results.csv exported")
