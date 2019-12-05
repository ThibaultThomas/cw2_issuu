import matplotlib.pyplot as plt


def showContinent(data: list) -> None:
    """

    :param data: The list of continents to show
    """
    showPlot(data, "Continent", "Occurrences", "Number of occurrences per Continent")


def showCountries(data: list) -> None:
    """

    :param data: The list of countries to show
    """
    showPlot(data, "Country", "Occurrences", "Number of occurrences per country")


def showUserAgents(data: list) -> None:
    """

    :param data: The list of user agents to show
    """
    showPlot(data, "Browser", "Occurrences", "Number of occurrences per browser")


def showBrowsers(data: list) -> None:
    """

    :param data: The list of browser to show
    """
    showPlot(data, "Browser", "Occurrences", "Number of occurrences per browser")


def showPlot(data: list, x_label: str, y_label: str, title: str) -> None:
    """

    :param data: The list of data to represent
    :param x_label: The title to set on the x Axis
    :param y_label: The title to set on the y Axis
    :param title: The window's title
    """
    values = {}
    for k in data:
        if k not in values:
            values[k] = 1
        else:
            values[k] += 1
    plt.figure()
    plt.style.use('ggplot')

    x = values.keys()
    energy = values.values()
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, energy, color='green')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    plt.xticks(x_pos, x)
    plt.show()
