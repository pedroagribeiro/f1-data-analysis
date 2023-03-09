import argparse
import fastf1
from fastf1 import plotting
from matplotlib import pyplot as plt

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog = 'Formula 1 - Fastest Race Lap Comparator',
        description = 'Establishes a detailed comparison of the fastest race lap between two drivers'
    )
    parser.add_argument('-year', type = int, action = 'store')
    parser.add_argument('-grand_prix', action = 'store')
    parser.add_argument('-session', action = 'store')
    parser.add_argument('-driver_1', action = 'store')
    parser.add_argument('-driver_2', action = 'store')
    args = parser.parse_args()
    print(args.grand_prix)
    return args

def enable_data_caching_and_setup_plotting():
    plotting.setup_mpl()
    fastf1.Cache.enable_cache("cache")

def collect_drivers_data_from_session(year, grand_prix, session, driver_1, driver_2):
    session_data = fastf1.get_session(year, grand_prix, session)
    session_laps = session_data.load_laps(with_telemetry = True)
    laps_driver_1 = session_laps.pick_driver(driver_1)
    laps_driver_2 = session_laps.pick_driver(driver_2)
    return laps_driver_1, laps_driver_2

def extract_fastest_laps(driver_1_data, driver_2_data):
    return driver_1_data.pick_fastest(), driver_2_data.pick_fastest()

def extract_laps_telemetry(driver_1_fastest, driver_2_fastest):
    return driver_1_fastest.get_car_data().add_distance(), driver_2_fastest.get_car_data().add_distance()

def plot_telemetry_comparison(grand_prix, session, driver_1, driver_2, driver_1_telemetry, driver_2_telemetry):
    fig, ax = plt.subplots(3)
    fig.suptitle("Fastest Session Lap Telemetry Comparison - " + grand_prix + " - " + session)
    ax[0].plot(driver_1_telemetry['Distance'], driver_1_telemetry['Speed'], label = driver_1)
    ax[0].plot(driver_2_telemetry['Distance'], driver_2_telemetry['Speed'], label = driver_2)
    ax[0].set(ylabel='Speed')
    ax[0].legend(loc="lower right")
    ax[1].plot(driver_1_telemetry['Distance'], driver_1_telemetry['Throttle'], label = driver_1)
    ax[1].plot(driver_2_telemetry['Distance'], driver_2_telemetry['Throttle'], label = driver_2)
    ax[1].set(ylabel='Throttle')
    ax[2].plot(driver_1_telemetry['Distance'], driver_1_telemetry['Brake'], label = driver_1)
    ax[2].plot(driver_2_telemetry['Distance'], driver_2_telemetry['Brake'], label = driver_2)
    ax[2].set(ylabel='Brakes')
    for a in ax.flat:
        a.label_outer()
    plt.show()


if __name__ == "__main__":
    enable_data_caching_and_setup_plotting()
    args = parse_arguments()
    driver_1_data, driver_2_data = collect_drivers_data_from_session(args.year, args.grand_prix, args.session, args.driver_1, args.driver_2)
    driver_1_fastest, driver_2_fastest = extract_fastest_laps(driver_1_data, driver_2_data)
    driver_1_telemetry, driver_2_telemetry = extract_laps_telemetry(driver_1_fastest, driver_2_fastest)
    plot_telemetry_comparison(args.grand_prix, args.session, args.driver_1, args.driver_2, driver_1_telemetry, driver_2_telemetry)
