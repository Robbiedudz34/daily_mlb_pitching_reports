import numpy as np

# Mathematical Equations for MLB Field Dimensions
def arizona_diamondbacks(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Arizona Diamondbacks.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 4.9:
        return -389.4197 / (np.sin(theta) - (1.1624468 * np.cos(theta)))
    elif 4.9 <= theta_deg < 6.6:
        return 423.5471 / (np.sin(theta) + (1.085346 * np.cos(theta)))
    elif 6.6 <= theta_deg < 31.7:
        return 6211.3885 / (np.sin(theta) + (17.49789 * np.cos(theta)))
    elif 31.7 <= theta_deg < 32.9:
        return 427.9667 / (np.sin(theta) + (0.630552 * np.cos(theta)))
    elif 32.9 <= theta_deg < 34.0:
        return 1197.8397 / (np.sin(theta) + (2.9286229 * np.cos(theta)))
    elif 34.0 <= theta_deg < 38.9:
        return 559.10919 / (np.sin(theta) + (1.0073058 * np.cos(theta)))
    elif 38.9 <= theta_deg < 39.1:
        return -91.557622 / (np.sin(theta) - (1.10398598 * np.cos(theta)))
    elif 39.1 <= theta_deg < 50.5:
        return 571.92441 / (np.sin(theta) + (1.0070058 * np.cos(theta)))
    elif 50.5 <= theta_deg < 50.8:
        return 114.59269 / (np.sin(theta) - (0.76826977 * np.cos(theta)))
    elif 50.8 <= theta_deg < 55.7:
        return 557.962 / (np.sin(theta) + (1.0031979 * np.cos(theta)))
    elif 55.7 <= theta_deg < 56.7:
        return 403.8808 / (np.sin(theta) + (0.3213439 * np.cos(theta)))
    elif 56.7 <= theta_deg < 57.7:
        return 755.17044 / (np.sin(theta) + (1.924966 * np.cos(theta)))
    elif 57.7 <= theta_deg < 82.5:
        return 353.793768 / (np.sin(theta) + (0.06108017 * np.cos(theta)))
    elif 82.5 <= theta_deg < 84.2:
        return 395.0241 / (np.sin(theta) + (0.9533913 * np.cos(theta)))
    elif 84.2 <= theta_deg < 90.0:
        return 327 / (np.sin(theta) - (0.9060869 * np.cos(theta)))
    else:
        return None

def athletics(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Athletics.
    My estimate based on available data.
    """
    data = [
        (0.0, 325.0),
        (1.0, 327.3),
        (2.0, 329.7),
        (3.0, 332.2),
        (4.0, 334.8),
        (5.0, 337.5),
        (6.0, 340.3),
        (7.0, 343.2),
        (8.0, 346.2),
        (9.0, 349.3),
        (9.9, 352.5),
        (10.9, 355.8),
        (11.9, 359.2),
        (12.8, 362.7),
        (13.8, 366.3),
        (14.7, 370.0),
        (15.7, 370.2),
        (16.7, 370.5),
        (17.7, 370.9),
        (18.7, 371.4),
        (19.7, 372.0),
        (20.7, 372.7),
        (21.7, 373.5),
        (22.7, 374.4),
        (23.7, 375.4),
        (24.7, 376.5),
        (25.8, 377.7),
        (26.9, 379.0),
        (28.0, 380.4),
        (29.0, 381.9),
        (30.0, 383.5),
        (31.0, 385.2),
        (32.0, 387.0),
        (33.0, 388.9),
        (34.0, 390.9),
        (35.0, 393.0),
        (36.0, 395.2),
        (37.0, 397.5),
        (38.0, 399.9),
        (39.0, 402.4),
        (40.0, 404.5),
        (41.0, 404.0),
        (42.0, 403.6),
        (43.0, 403.3),
        (44.0, 403.1),
        (45.0, 403.0),
        (46.0, 403.1),
        (47.0, 403.3),
        (48.0, 403.6),
        (49.0, 404.0),
        (50.0, 404.5),
        (51.0, 405.0),
        (52.0, 403.9),
        (53.0, 402.8),
        (54.0, 401.8),
        (55.0, 400.7),
        (56.0, 399.6),
        (57.0, 398.5),
        (58.0, 397.4),
        (59.0, 396.2),
        (60.0, 395.0),
        (61.0, 393.8),
        (62.0, 392.5),
        (63.0, 391.2),
        (64.0, 389.8),
        (65.0, 388.3),
        (66.0, 386.8),
        (67.0, 385.2),
        (68.0, 383.6),
        (69.0, 381.8),
        (70.0, 380.0),
        (71.0, 378.1),
        (72.0, 376.1),
        (73.0, 374.0),
        (74.0, 371.9),
        (75.0, 369.8),
        (76.0, 367.8),
        (77.0, 365.7),
        (78.0, 363.7),
        (79.0, 361.8),
        (80.0, 360.0),
        (81.0, 358.3),
        (82.0, 356.5),
        (83.0, 354.7),
        (84.0, 352.5),
        (85.0, 350.0),
        (86.0, 347.0),
        (87.0, 343.6),
        (88.0, 340.0),
        (89.0, 336.0),
        (90.0, 330.0)
    ]
        # Return None if out of bounds
    if theta_deg < 0 or theta_deg > 90:
        return None

    # Interpolate linearly between the two surrounding points
    for i in range(len(data) - 1):
        theta1, r1 = data[i]
        theta2, r2 = data[i + 1]
        if theta1 <= theta_deg <= theta2:
            # Linear interpolation
            t = (theta_deg - theta1) / (theta2 - theta1)
            return r1 + t * (r2 - r1)

    return None  # fallback

def atlanta_braves(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Atlanta Braves.
    
    My estimate - no fangraphs data available.
    """
    data = [
        (0, 325),
        (23, 375),
        (38, 402),
        (51, 402),
        (66, 385),
        (76, 380),
        (90, 335)
    ]

    # Return None if out of bounds
    if theta_deg < 0 or theta_deg > 90:
        return None

    # Interpolate linearly between the two surrounding points
    for i in range(len(data) - 1):
        theta1, r1 = data[i]
        theta2, r2 = data[i + 1]
        if theta1 <= theta_deg <= theta2:
            # Linear interpolation
            t = (theta_deg - theta1) / (theta2 - theta1)
            return r1 + t * (r2 - r1)

    return None  # fallback

def baltimore_orioles(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Baltimore Orioles.
    My estimate based on available data.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 25.5:
        return -1786.977 / (np.sin(theta) - (5.61942 * np.cos(theta)))
    elif 25.5 <= theta_deg < 49.0:
        return 801.702 / (np.sin(theta) + (1.830 * np.cos(theta)))
    elif 49.0 <= theta_deg < 69.7:
        return 359.7761 / (np.sin(theta) + (0.187168 * np.cos(theta)))
    elif 69.7 <= theta_deg < 90.0:
        data = [
            (69.7, 363),
            (69.8, 364),
            (69.9, 366),
            (70.0, 368),
            (70.1, 370),
            (70.2, 372),
            (70.3, 374),
            (72.3, 373),
            (74.3, 372),
            (76.3, 371),
            (78.4, 370.75),
            (80.5, 370.5),
            (82.5, 371.25),
            (84.5, 372.25),
            (86.5, 373),
            (87.5, 358),
            (88.5, 345),
            (89.5, 333),
            (90, 331)
        ]
        for i in range(len(data) - 1):
            theta1, r1 = data[i]
            theta2, r2 = data[i + 1]
            if theta1 <= theta_deg <= theta2:
                # Linear interpolation
                t = (theta_deg - theta1) / (theta2 - theta1)
                return r1 + t * (r2 - r1)
    else:
        return None

def boston_red_sox(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Boston Red Sox.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 3.8:
        return -119.0423 / (np.sin(theta) - (0.3941798 * np.cos(theta)))
    elif 3.8 <= theta_deg < 4.9:
        return -402.289 / (np.sin(theta) - (1.17404 * np.cos(theta)))
    elif 4.9 <= theta_deg < 6.0:
        return -808.953 / (np.sin(theta) - (2.274195 * np.cos(theta)))
    elif 6.0 <= theta_deg < 7.1:
        return -2332.79083 / (np.sin(theta) - (6.3601456 * np.cos(theta)))
    elif 7.1 <= theta_deg < 8.1:
        return -20759.85313 / (np.sin(theta) - (55.616 * np.cos(theta)))
    elif 8.1 <= theta_deg < 31.0:
        return 1129.33168 / (np.sin(theta) + (2.875435 * np.cos(theta)))
    elif 31.0 <= theta_deg < 33.8:
        return -417.143116 / (np.sin(theta) - (1.8849057 * np.cos(theta)))
    elif 33.8 <= theta_deg < 52.2:
        return 431.2604 / (np.sin(theta) + (0.587157 * np.cos(theta)))
    elif 52.2 <= theta_deg < 53.1:
        return 2077.8716 / (np.sin(theta) + (7.7513156 * np.cos(theta)))
    elif 53.1 <= theta_deg < 90.0:
        return 306 / (np.sin(theta) - (0.00577087 * np.cos(theta)))
    else:
        return None

def chicago_cubs(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Chicago Cubs.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 10.9:
        return -4499.412 / (np.sin(theta) - (12.7462 * np.cos(theta)))
    elif 10.9 <= theta_deg < 13.1:
        return 297.1748 / (np.sin(theta) + (0.636566 * np.cos(theta)))
    elif 13.1 <= theta_deg < 29.4:
        return 18363.859 / (np.sin(theta) + (53.4839 * np.cos(theta)))
    elif 29.4 <= theta_deg < 49.2:
        denominator = 33526.25 - 9105.75 * np.cos(2 * theta - np.pi)
        term1 = (
            9353823.75 * np.cos(theta - np.radians(33.2)) -
            2540504.25 * np.cos(theta - np.radians(146.8))
        )
        sin_term = np.sin(theta - np.radians(33.2))
        term2 = 22815 * np.sqrt(denominator - 155682 * sin_term**2)

        return (term1 + term2) / denominator
    elif 49.2 <= theta_deg < 73.2:
        return 357.8732 / (np.sin(theta) + (0.245827 * np.cos(theta)))
    elif 73.2 <= theta_deg < 74.8:
        return 496.86435 / (np.sin(theta) + (1.62768 * np.cos(theta)))
    elif 74.8 <= theta_deg < 90.0:
        return 355 / (np.sin(theta) + (0.112061 * np.cos(theta)))
    else:
        return None

def chicago_white_sox(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Chicago White Sox.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 24.1:
        return -7014.6043 / (np.sin(theta) - (20.939117 * np.cos(theta)))
    elif 24.1 <= theta_deg < 30.6:
        return 1495.6997 / (np.sin(theta) + (3.92207 * np.cos(theta)))
    elif 30.6 <= theta_deg < 36.6:
        return 820.061 / (np.sin(theta) + (1.88324 * np.cos(theta)))
    elif 36.6 <= theta_deg < 39.1:
        return 1969.1459 / (np.sin(theta) + (5.562717 * np.cos(theta)))
    elif 39.1 <= theta_deg < 50.6:
        return 561.4969 / (np.sin(theta) + (1.00525 * np.cos(theta)))
    elif 50.6 <= theta_deg < 54.0:
        return 363.2118 / (np.sin(theta) + (0.2203438 * np.cos(theta)))
    elif 54.0 <= theta_deg < 58.7:
        return 426.18439 / (np.sin(theta) + (0.49718 * np.cos(theta)))
    elif 58.7 <= theta_deg < 63.4:
        return 378.8179 / (np.sin(theta) + (0.259128 * np.cos(theta)))
    elif 63.4 <= theta_deg < 79.0:
        return 340.82399 / (np.sin(theta) + (0.03285 * np.cos(theta)))
    elif 79.0 <= theta_deg < 90.0:
        return 327 / (np.sin(theta) - (0.177146 * np.cos(theta)))
    else:
        return None

def cincinnati_reds(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Cincinnati Reds.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 44.7:
        denominator = 41212.25 - 30987.75 * np.cos(2 * theta - np.radians(190))
        term1 = (
            11951552.5 * np.cos(theta - np.radians(25.2)) -
            8986447.5 * np.cos(theta - np.radians(164.8))
        )
        sin_term = np.sin(theta - np.radians(25.2))
        term2 = 19212.09 * np.sqrt(denominator - 168200 * sin_term**2)
        
        return (term1 + term2) / denominator
    elif 44.7 <= theta_deg < 60.3:
        return 436.311 / (np.sin(theta) + (0.52231577 * np.cos(theta)))
    elif 60.3 <= theta_deg < 86.6:
        return 336.435 / (np.sin(theta) + (0.0014347 * np.cos(theta)))
    elif 86.6 <= theta_deg < 90.0:
        return 326 / (np.sin(theta) - (0.5206991 * np.cos(theta)))
    else:
        return None

def cleveland_guardians(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Cleveland Guardians.
    """
    theta = np.radians(theta_deg)

    if 0.0 <= theta_deg < 20.3:
        return -1609.844 / (np.sin(theta) - (4.98404 * np.cos(theta)))
    elif 20.3 <= theta_deg < 48.25:
        return 906.183 / (np.sin(theta) + (2.2274 * np.cos(theta)))
    elif 48.25 <= theta_deg < 78.25:
        return 356.7465 / (np.sin(theta) + (0.197554 * np.cos(theta)))
    elif 78.25 <= theta_deg < 90.0:
        return 321 / (np.sin(theta) - (0.303978 * np.cos(theta)))
    else:
        return None

def colorado_rockies(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Colorado Rockies.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 1.25:
        return -551.417 / (np.sin(theta) - (1.57548 * np.cos(theta)))
    elif 1.25 <= theta_deg < 37.5:
        return 4061.537 / (np.sin(theta) + (11.422 * np.cos(theta)))
    elif 37.5 <= theta_deg < 60.2:
        return 536.536 / (np.sin(theta) + (0.84288 * np.cos(theta)))
    elif 60.2 <= theta_deg < 90.0:
        return 345 / (np.sin(theta) - (0.08135 * np.cos(theta)))
    else:
        return None

def detroit_tigers(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Detroit Tigers.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 1.25:
        return -405.584 / (np.sin(theta) - (1.23813 * np.cos(theta)))
    elif 1.25 <= theta_deg < 22.5:
        return 337.21 / np.cos(theta)
    elif 22.5 <= theta_deg < 24.6:
        return -430.4868 / (np.sin(theta) - (1.6908 * np.cos(theta)))
    elif 24.6 <= theta_deg < 35.3:
        return 347.675 / np.cos(theta)
    elif 35.3 <= theta_deg < 54.0:
        return 593.97 / (np.sin(theta) + np.cos(theta))
    elif 54.0 <= theta_deg < 90.0:
        return 345 / np.sin(theta)
    else:
        return None

def houston_astros(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Houston Astros.
    Using my own estimates based on available data.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 23:
        return -2738.7177 / (np.sin(theta) - (8.400974 * np.cos(theta)))
    elif 23 <= theta_deg < 24.1:
        return 315.172 / (np.sin(theta) + (0.493462 * np.cos(theta)))
    elif 24.1 <= theta_deg < 34.0:
        return -2943.702 / (np.sin(theta) - (9.23423 * np.cos(theta)))
    # Equation determined without fangraphs data
    elif 34.0 <= theta_deg < 50.2:
        return 588.57 / (np.sin(theta) + (1.038 * np.cos(theta)))
    elif 50.2 <= theta_deg < 67.7:
        return 347.579 / (np.sin(theta) + (0.120385 * np.cos(theta)))
    elif 67.7 <= theta_deg < 67.9:
        return 42.673422 / (np.sin(theta) - (2.124119 * np.cos(theta)))
    elif 67.9 <= theta_deg < 90.0:
        return 315 / (np.sin(theta) - (0.0366002 * np.cos(theta)))
    else:
        return None
    
def kansas_city_royals(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Kansas City Royals.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 5.9:
        denominator = 5417 - 1545 * np.cos(2 * theta - np.pi)
        term1 = (
            1738857 * np.cos(theta - np.radians(10.1)) -
            495945 * np.cos(theta - np.radians(169.9))
        )
        term2 = 3671.3 * np.sqrt(denominator - 206082 * np.sin(theta - np.radians(10.1))**2)
                
        return (term1 + term2) / denominator
    elif 5.9 <= theta_deg < 22.1:
        return 25784.376 / (np.sin(theta) + (71.503534 * np.cos(theta)))
    elif 22.1 <= theta_deg < 59.0:
        denominator = 111634 - 10384 * np.cos(2 * theta + np.radians(26))
        term1 = (
            19759218 * np.cos(theta - np.radians(50.9)) -
            1837968 * np.cos(theta + np.radians(76.9))
        )
        term2 = 78594.9 * np.sqrt(denominator - 62658 * np.sin(theta - np.radians(50.9))**2)
                
        return (term1 + term2) / denominator
    elif 59.0 <= theta_deg < 76.9:
        denominator = 16218 - 14040 * np.cos(2 * theta + np.radians(12))
        term1 = (
            5642864 * np.cos(theta - np.radians(68.7)) -
            4885920 * np.cos(theta + np.radians(80.7))
        )
        term2 = 5740.3 * np.sqrt(denominator - 242208 * np.sin(theta - np.radians(68.7))**2)
                
        return (term1 + term2) / denominator
    elif 76.9 <= theta_deg < 82.7:
        return 361.884 / (np.sin(theta) + (0.01803985 * np.cos(theta)))
    elif 82.7 <= theta_deg < 90.0:
        denominator = 2897 - 975 * np.cos(2 * theta - np.radians(38))
        term1 = (
            958907 * np.cos(theta - np.radians(82.6)) -
            322725 * np.cos(theta + np.radians(44.6))
        )
        term2 = 1929 * np.sqrt(denominator - 219122 * np.sin(theta - np.radians(82.6))**2)
                
        return (term1 + term2) / denominator
    else:
        return None
    
def los_angeles_angels(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Los Angeles Angels.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 1.6:
        return -352.2388 / (np.sin(theta) - (1.06739 * np.cos(theta)))
    elif 1.6 <= theta_deg < 3.2:
        return -496.7696 / (np.sin(theta) - (1.493901 * np.cos(theta)))
    elif 3.2 <= theta_deg < 4.8:
        return -641.02615 / (np.sin(theta) - (1.9114787 * np.cos(theta)))
    elif 4.8 <= theta_deg < 6.6:
        return -1020.3203 / (np.sin(theta) - (2.9928111 * np.cos(theta)))
    elif 6.6 <= theta_deg < 11.2:
        return 6919.533 / (np.sin(theta) + (19.3875915 * np.cos(theta)))
    elif 11.2 <= theta_deg < 42.6:
        return 1240.50705 / (np.sin(theta) + (3.314747 * np.cos(theta)))
    elif 42.6 <= theta_deg < 68.0:
        return 437.37565 / (np.sin(theta) + (0.5733725 * np.cos(theta)))
    elif 68.0 <= theta_deg < 84.0:
        return 351.0005 / (np.sin(theta) - (0.0286525 * np.cos(theta)))
    elif 84.0 <= theta_deg < 85.6:
        return 340.789 / (np.sin(theta) - (0.3046164 * np.cos(theta)))
    elif 85.6 <= theta_deg < 87.0:
        return 329.5441 / (np.sin(theta) - (0.72339596 * np.cos(theta)))
    elif 87.0 <= theta_deg < 88.4:
        return 324.50638 / (np.sin(theta) - (1.0040283 * np.cos(theta)))
    elif 88.4 <= theta_deg < 90.0:
        return 328 / (np.sin(theta) - (0.629411 * np.cos(theta)))
    else:
        return None

def los_angeles_dodgers(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Los Angeles Dodgers.
    """
    theta = np.radians(theta_deg)
    
    if 0 <= theta_deg < 4.2:
        return -443.8081 / (np.sin(theta) - (1.344873 * np.cos(theta)))
    elif 4.2 <= theta_deg < 7.8:
        return -829.5118 / (np.sin(theta) - (2.44985 * np.cos(theta)))
    elif 7.8 <= theta_deg < 9.5:
        return -10942.3745 / (np.sin(theta) - (30.646819 * np.cos(theta)))
    elif 9.5 <= theta_deg < 25.1:
        return 1719.756 / (np.sin(theta) + (4.622957 * np.cos(theta)))
    elif 25.1 <= theta_deg < 31.1:
        return 1115.073 / (np.sin(theta) + (2.83277 * np.cos(theta)))
    elif 31.1 <= theta_deg < 42.6:
        return 928.868 / (np.sin(theta) + (2.258998 * np.cos(theta)))
    elif 42.6 <= theta_deg < 44.0:
        return 742.26267 / (np.sin(theta) + (1.620443 * np.cos(theta)))
    elif 44 <= theta_deg < 46.3:
        return 562.6864 / (np.sin(theta) + (0.9947777 * np.cos(theta)))
    elif 46.3 <= theta_deg < 49.2:
        return 472.8006 / (np.sin(theta) + (0.66870534 * np.cos(theta)))
    elif 49.2 <= theta_deg < 55.3:
        return 423.6147 / (np.sin(theta) + (0.478618 * np.cos(theta)))
    elif 55.3 <= theta_deg < 59:
        return 395.11776 / (np.sin(theta) + (0.349269 * np.cos(theta)))
    elif 59 <= theta_deg < 63.1:
        return 392.2193 / (np.sin(theta) + (0.3344991 * np.cos(theta)))
    elif 63.1 <= theta_deg < 69.2:
        return 381.7462 / (np.sin(theta) + (0.2729345 * np.cos(theta)))
    elif 69.2 <= theta_deg < 74.7:
        return 372.8431 / (np.sin(theta) + (0.2051737 * np.cos(theta)))
    elif 74.7 <= theta_deg < 80.5:
        return 368.8506 / (np.sin(theta) + (0.163833 * np.cos(theta)))
    elif 80.5 <= theta_deg < 82.1:
        return 362.2344 / (np.sin(theta) + (0.053704 * np.cos(theta)))
    elif 82.1 <= theta_deg < 83.3:
        return 353.007 / (np.sin(theta) - (0.131245 * np.cos(theta)))
    elif 83.3 <= theta_deg < 85.6:
        return 334.774 / (np.sin(theta) - (0.564136 * np.cos(theta)))
    elif 85.6 <= theta_deg < 87.2:
        return 333.006 / (np.sin(theta) - (0.629807 * np.cos(theta)))
    elif 87.2 <= theta_deg < 88.4:
        return 328.317 / (np.sin(theta) - (0.90885 * np.cos(theta)))
    elif 88.4 <= theta_deg < 90:
        return 330 / (np.sin(theta) - (0.729958 * np.cos(theta)))
    
def miami_marlins(theta_deg):
    """    
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Miami Marlins.
    My estimate based on available data.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 23.7:
        return -3285.092 / (np.sin(theta) - (9.80624 * np.cos(theta)))
    elif 23.7 <= theta_deg < 59:
        data = [
            (23.7, 383),
            (35, 391),
            (40.0, 397),
            (43.0, 399),
            (45.0, 400),
            (47.0, 399),
            (50.0, 397),
            (55, 391),
            (59, 387),
        ]
        # Interpolate linearly between the two surrounding points
        for i in range(len(data) - 1):
            theta1, r1 = data[i]
            theta2, r2 = data[i + 1]
            if theta1 <= theta_deg <= theta2:
                # Linear interpolation
                t = (theta_deg - theta1) / (theta2 - theta1)
                return r1 + t * (r2 - r1)
    elif 59 <= theta_deg < 60.8:
        return 389.587 / (np.sin(theta) + (0.2903055 * np.cos(theta)))
    elif 60.8 <= theta_deg < 63.6:
        return 387.8902 / (np.sin(theta) + (0.281246 * np.cos(theta)))
    elif 63.6 <= theta_deg < 68.2:
        return 367.932 / (np.sin(theta) + (0.163124 * np.cos(theta)))
    elif 68.2 <= theta_deg < 72.1:
        return 360.9411 / (np.sin(theta) + (0.112519 * np.cos(theta)))
    elif 72.1 <= theta_deg < 79.2:
        return 349.332 / (np.sin(theta) + (0.00931917 * np.cos(theta)))
    elif 79.2 <= theta_deg < 84.3:
        return 339.562 / (np.sin(theta) - (0.137541 * np.cos(theta)))
    elif 84.3 <= theta_deg < 90.0:
        return 337 / (np.sin(theta) - (0.212114 * np.cos(theta)))
    else:
        return None   

def milwaukee_brewers(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Milwaukee Brewers.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 16.5:
        return 4068.1011 / (np.sin(theta) + (11.7916 * np.cos(theta)))
    elif 16.5 <= theta_deg < 16.8:
        return -60.8626 / (np.sin(theta) - (0.47706 * np.cos(theta)))
    elif 16.8 <= theta_deg < 23.3:
        return 3834.475 / (np.sin(theta) + (10.73232 * np.cos(theta)))
    elif 23.3 <= theta_deg < 35.5:
        return 1042.985 / (np.sin(theta) + (2.60569 * np.cos(theta)))
    elif 35.5 <= theta_deg < 37.7:
        return -1107.4106 / (np.sin(theta) - (4.237288 * np.cos(theta)))
    elif 37.7 <= theta_deg < 52.3:
        return 566.71123 / (np.sin(theta) + np.cos(theta))
    elif 52.3 <= theta_deg < 56.2:
        return 287.52 / (np.sin(theta) - (0.130068 * np.cos(theta)))
    elif 56.2 <= theta_deg < 74:
        return 393.82239 / (np.sin(theta) + (0.374126 * np.cos(theta)))
    elif 74 <= theta_deg < 85:
        return 358.50448 / (np.sin(theta) + (0.027824 * np.cos(theta)))
    elif 85 <= theta_deg < 90:
        return 344 / (np.sin(theta) - (0.435742 * np.cos(theta)))
    else:
        return None   
    
def minnesota_twins(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Minnesota Twins.
    Placeholder values for manual input.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 20.0:
        return -2731.998 / (np.sin(theta) - 8.3292 * np.cos(theta))
    elif 20.0 <= theta_deg < 38.5:
        return 1691.285 / (np.sin(theta) + 4.5671 * np.cos(theta))
    elif 38.5 <= theta_deg < 51.2:
        return 629.3765 / (np.sin(theta) + 1.2001 * np.cos(theta))
    elif 51.2 <= theta_deg < 67.0:
        return 382.741 / (np.sin(theta) + 0.24243 * np.cos(theta))
    elif 67.0 <= theta_deg <= 90.0:
        return 339 / (np.sin(theta) - 0.05451 * np.cos(theta))
    else:
        return None
       
def new_york_mets(theta_deg):
    """
    Return the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the New York Mets.
    """
    theta = np.radians(theta_deg)
    
    if 0 <= theta_deg < 18.8:
        return -1967.79 / (np.sin(theta) - (5.963 * np.cos(theta)))
    elif 18.8 <= theta_deg < 23:
        return 667.7078 / (np.sin(theta) + (1.566132 * np.cos(theta)))
    elif 23 <= theta_deg < 40.6:
        return 1795.74 / (np.sin(theta) + (4.923 * np.cos(theta)))
    elif 40.6 <= theta_deg < 49.1:
        return 575.86589 / (np.sin(theta) + (0.9960149 * np.cos(theta)))
    elif 49.1 <= theta_deg < 82.1:
        return 358.6125 / (np.sin(theta) + (0.1847292 * np.cos(theta)))
    elif 82.1 <= theta_deg < 90:
        return 335 / (np.sin(theta) - (0.30194697 * np.cos(theta)))
    else:
        return None
    
def new_york_yankees(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the New York Yankees.
    Placeholder values for manual input.
    """
    theta = np.radians(theta_deg)

    if 0.0 <= theta_deg < 3.2:
        return -752.7415 / (np.sin(theta) - 2.397266 * np.cos(theta))
    elif 3.2 <= theta_deg < 4.9:
        return -1341.4764 / (np.sin(theta) - 4.22849 * np.cos(theta))
    elif 4.9 <= theta_deg < 30.6:
        return 323.639 / np.cos(theta)
    elif 30.6 <= theta_deg < 36.1:
        return 2683.6147 / (np.sin(theta) + 7.700602 * np.cos(theta))
    elif 36.1 <= theta_deg < 40.4:
        return 913.27186 / (np.sin(theta) + 2.139572 * np.cos(theta))
    elif 40.4 <= theta_deg < 44.4:
        return 707.36801 / (np.sin(theta) + 1.4653105 * np.cos(theta))
    elif 44.4 <= theta_deg < 48.4:
        return 600.6388 / (np.sin(theta) + 1.096466 * np.cos(theta))
    elif 48.4 <= theta_deg < 52.1:
        return 496.311752 / (np.sin(theta) + 0.7103818 * np.cos(theta))
    elif 52.1 <= theta_deg < 56.7:
        return 445.2994 / (np.sin(theta) + 0.5053365 * np.cos(theta))
    elif 56.7 <= theta_deg < 62.8:
        return 390.30014 / (np.sin(theta) + 0.2548946 * np.cos(theta))
    elif 62.8 <= theta_deg < 80.6:
        return 345.39856 / (np.sin(theta) + 0.001719809 * np.cos(theta))
    elif 80.6 <= theta_deg < 84.8:
        return 324.4985 / (np.sin(theta) - 0.3638949 * np.cos(theta))
    elif 84.8 <= theta_deg <= 90.0:
        return 316 / (np.sin(theta) - 0.6421415 * np.cos(theta))
    else:
        return None
    
def philadelphia_phillies(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Philadelphia Phillies.
    Placeholder values for manual input.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 34.3:
        return 330 / np.cos(theta)
    elif 34.3 <= theta_deg < 50.7:
        return 644.15 / (np.sin(theta) + 1.277017 * np.cos(theta))
    elif 50.7 <= theta_deg < 55.9:
        return 308.591 / (np.sin(theta) - 0.02468 * np.cos(theta))
    elif 55.9 <= theta_deg < 59.3:
        return 543.4657 / (np.sin(theta) + 1.08071 * np.cos(theta))
    elif 59.3 <= theta_deg < 88.3:
        return 331 / np.sin(theta)
    elif 88.3 <= theta_deg <= 90.0:
        return 325 / (np.sin(theta) - 0.596191 * np.cos(theta))
    else:
        return None

def pittsburgh_pirates(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Pittsburgh Pirates.
    My estimate based on available data.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 22.3:
        return -1759.947 / (np.sin(theta) - (5.4827 * np.cos(theta)))
    elif 22.3 <= theta_deg < 34.1:
        return 1120.149 / (np.sin(theta) + (2.8184 * np.cos(theta)))
    elif 34.1 <= theta_deg < 44.3:
        return 716.884 / (np.sin(theta) + (1.56 * np.cos(theta)))
    elif 44.3 <= theta_deg < 58.5:
        return 478.809 / (np.sin(theta) + (0.71785 * np.cos(theta)))
    elif 58.5 <= theta_deg < 59.6:
        return -4560.837 / (np.sin(theta) - (24.0136 * np.cos(theta)))
    elif 59.6 <= theta_deg < 81.5:
        return 366.846 / (np.sin(theta) + (0.089958 * np.cos(theta)))
    elif 81.5 <= theta_deg < 90.0:
        return 321 / (np.sin(theta) - (0.75751 * np.cos(theta)))
    else:
        return None

def san_diego_padres(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the San Diego Padres.
    My estimate based on available data.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 3.4:
        return 321.433 / np.cos(theta)
    elif 3.4 <= theta_deg < 7.2:
        return -311.7359 / (np.sin(theta) - (1.029242 * np.cos(theta)))
    elif 7.2 <= theta_deg < 27.8:
        return 345.87116 / np.cos(theta)
    elif 27.8 <= theta_deg < 31.8:
        return 1425.7353 / (np.sin(theta) + (3.59492 * np.cos(theta)))
    elif 31.8 <= theta_deg < 38.3:
        return 740.2202 / (np.sin(theta) + (1.568308 * np.cos(theta)))
    elif 38.3 <= theta_deg < 49.2:
        return 543.05468 / (np.sin(theta) + (0.9402139 * np.cos(theta)))
    elif 49.2 <= theta_deg < 50.4:
        return 318.3662 / (np.sin(theta) + (0.0718681 * np.cos(theta)))
    elif 50.4 <= theta_deg < 56.2:
        return 539.44852 / (np.sin(theta) + (0.9611939 * np.cos(theta)))
    elif 56.2 <= theta_deg < 63.5:
        return 393.566469 / (np.sin(theta) + (0.2972994 * np.cos(theta)))
    elif 63.5 <= theta_deg < 83.8:
        return 344.316 / (np.sin(theta) + (0.0091906 * np.cos(theta)))
    elif 83.8 <= theta_deg <= 90.0:
        return 336 / (np.sin(theta) - (0.2134522 * np.cos(theta)))
    else:
        return None    
    
def san_francisco_giants(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the San Francisco Giants.
    My estimate based on available data.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 15.0:
        return -697.339 / (np.sin(theta) - (2.25676 * np.cos(theta)))
    elif 15.0 <= theta_deg < 18.0:
        return 946.0859 / (np.sin(theta) + (2.4155 * np.cos(theta)))
    elif 18.0 <= theta_deg < 25.6:
        return -712.5915 / (np.sin(theta) - (2.3890 * np.cos(theta)))
    elif 25.6 <= theta_deg < 56.2:
        return 552.5 / (np.sin(theta) + np.cos(theta))
    elif 56.2 <= theta_deg < 86.5:
        return 347.526 / (np.sin(theta) + (0.07905 * np.cos(theta)))
    elif 56.2 <= theta_deg < 90.0:
        return 335 / (np.sin(theta) - (0.513097 * np.cos(theta)))
    else:
        return None
    
def seattle_mariners(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Seattle Mariners.
    My estimate based on available data.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 26.5:
        return -3502.437 / (np.sin(theta) - (10.74367 * np.cos(theta)))
    elif 26.5 <= theta_deg < 47.0:
        return 825.224 / (np.sin(theta) + (1.9153 * np.cos(theta)))
    elif 47.0 <= theta_deg < 59.6:
        return 414.271 / (np.sin(theta) + (0.427476 * np.cos(theta)))
    elif 59.6 <= theta_deg < 66.5:
        return 377.4922 / (np.sin(theta) + (0.2382 * np.cos(theta)))
    elif 66.5 <= theta_deg < 88.5:
        return 336.558 / (np.sin(theta) - (0.037016 * np.cos(theta)))
    elif 88.5 <= theta_deg <= 90.0:
        return 331 / (np.sin(theta) - (0.6671 * np.cos(theta)))
    else:
        return None
    
def st_louis_cardinals(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the St. Louis Cardinals.
    My estimate based on available data.
    """
    theta = np.radians(theta_deg)

    if 0.0 <= theta_deg < 3.3:
        return -436.689 / (np.sin(theta) - (1.3173 * np.cos(theta)))
    elif 3.3 <= theta_deg < 25.6:
        return 346.303 / np.cos(theta)
    elif 25.6 <= theta_deg < 39.9:
        return 857.076 / (np.sin(theta) + (1.995805 * np.cos(theta)))
    elif 39.9 <= theta_deg < 50.0:
        return 569.534 / (np.sin(theta) + (1.04571 * np.cos(theta)))
    elif 50.0 <= theta_deg < 64.0:
        return 434.192 / (np.sin(theta) + (0.514 * np.cos(theta)))
    elif 64.0 <= theta_deg < 88.4:
        return 346.76 / np.sin(theta)
    elif 88.4 <= theta_deg <= 90.0:
        return 330 / (np.sin(theta) - (1.73033 * np.cos(theta)))
    else:
        return None
    
def tampa_bay_rays(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Tampa Bay Rays.
    My estimate based on available data.
    """
    data = [
        (0.0, 314),
        (1.8, 322),
        (3.6, 329),
        (5.4, 336),
        (6.6, 339),
        (7.4, 341),
        (8.4, 341.9),
        (9.4, 343),
        (10.4, 344.1),
        (11.4, 345.3),
        (12.4, 346.7),
        (13.4, 348.2),
        (14.4, 349.8),
        (15.4, 351.5),
        (16.4, 353.3),
        (17.4, 355.1),
        (18.4, 357),
        (19.4, 359),
        (20.4, 361.1),
        (21.4, 363.3),
        (22.4, 365.6),
        (23.4, 368),
        (24.4, 370.5),
        (25.4, 373.1),
        (26.4, 375.8),
        (27.4, 378.6),
        (28.4, 381.5),
        (29.4, 384.5),
        (30.4, 387.6),
        (32.8, 393),
        (35.2, 398),
        (37.2, 402),
        (39.2, 404),
        (42.0, 406),
        (45.0, 408),
        (46.0, 407.5),
        (48.0, 407),
        (51.0, 406),
        (53.2, 405),
        (55.2, 403.8),        
        (57.2, 402.4),
        (59.2, 400.8),
        (61.2, 398.8),
        (63.0, 396.0),
        (64.0, 392.4),
        (65.0, 388.9),
        (66.0, 385.5),
        (67.0, 382.3),
        (68.0, 379.1),
        (69.0, 376.1),
        (70.0, 373.1),
        (71.0, 370.2),
        (72.0, 367.4),
        (73.0, 364.7),
        (74.0, 362.1),
        (75.0, 359.5),
        (76.0, 357.0),
        (77.0, 354.6),
        (78.0, 352.3),
        (79.0, 350.1),
        (80.0, 348.5),
        (82.0, 345),
        (84.0, 340),
        (86.0, 334),
        (88.0, 327),
        (90.0, 318)       
    ]
    
    # Return None if out of bounds
    if theta_deg < 0 or theta_deg > 90:
        return None

    # Interpolate linearly between the two surrounding points
    for i in range(len(data) - 1):
        theta1, r1 = data[i]
        theta2, r2 = data[i + 1]
        if theta1 <= theta_deg <= theta2:
            # Linear interpolation
            t = (theta_deg - theta1) / (theta2 - theta1)
            return r1 + t * (r2 - r1)

    return None  # fallback

def texas_rangers(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Texas Rangers.
    My estimate based on available data.
    """
    data = [
        (0.0, 326.0),
        (1.1, 331.25),
        (2.2, 337.25),
        (3.3, 343.1),
        (4.3, 343.7),
        (5.3, 344.3),
        (6.3, 345.0),
        (7.3, 345.8),
        (8.3, 346.5),
        (9.4, 347.4),
        (10.4, 348.4),
        (11.4, 349.5),
        (12.4, 350.7),
        (13.4, 351.9),
        (14.4, 353.2),
        (15.4, 354.6),
        (16.4, 356.1),
        (17.4, 357.7),
        (18.4, 359.3),
        (19.4, 361.1),
        (20.5, 363.0),
        (21.5, 365.0),
        (22.5, 367.1),
        (23.5, 369.3),
        (24.5, 371.6),
        (25.5, 374.0),
        (26.0, 372.0),
        (26.6, 369.1),
        (27.2, 366.7),
        (28.0, 364.0),
        (29.0, 368.1),
        (30.0, 372.3),
        (31.0, 376.6),
        (32.0, 381.0),
        (33.0, 385.5),
        (34.0, 390.1),
        (35.0, 394.8),
        (36.0, 399.7),
        (37.0, 404.8),
        (38.0, 410.0),        
        (39.0, 409.3),
        (40.0, 408.7),
        (41.0, 408.2),
        (42.0, 407.8),
        (43.0, 407.5),
        (44.0, 407.2),
        (45.0, 407.0),
        (46.0, 407.2),
        (47.0, 407.5),
        (48.0, 407.8),
        (49.0, 408.2),
        (50.0, 408.7),
        (51.0, 409.3),
        (52.0, 410.0),
        (53.0, 406.8),
        (54.0, 403.6),
        (55.0, 400.5),
        (56.0, 397.5),
        (57.0, 394.6),
        (58.0, 391.8),
        (59.0, 389.1),
        (60.0, 386.5),
        (61.0, 384.0),
        (62.0, 381.6),
        (63.0, 379.3),
        (64.0, 377.1),
        (65.0, 375.0),
        (65.2, 372.0),
        (66.2, 369.8),
        (67.2, 367.7),
        (68.2, 365.7),
        (69.2, 363.8),
        (70.2, 362.0),
        (71.2, 360.3),
        (72.2, 358.7),
        (73.2, 357.2),
        (74.2, 355.8),
        (75.2, 354.5),
        (76.2, 353.3),
        (77.2, 352.2),
        (78.2, 351.2),
        (79.2, 350.3),
        (80.2, 349.5),
        (81.2, 348.8),
        (82.3, 346.7),
        (83.4, 344.5),
        (84.5, 342.2),
        (85.6, 339.8),
        (86.7, 337.3),
        (87.8, 334.7),
        (88.9, 331.9),
        (90.0, 329.0)
    ]
        # Return None if out of bounds
    if theta_deg < 0 or theta_deg > 90:
        return None

    # Interpolate linearly between the two surrounding points
    for i in range(len(data) - 1):
        theta1, r1 = data[i]
        theta2, r2 = data[i + 1]
        if theta1 <= theta_deg <= theta2:
            # Linear interpolation
            t = (theta_deg - theta1) / (theta2 - theta1)
            return r1 + t * (r2 - r1)

    return None  # fallback

def toronto_blue_jays(theta_deg):
    """
    Returns the distance"r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Toronto Blue Jays.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 20:
        return -1725.1974 / (np.sin(theta) - (5.2597 * np.cos(theta)))
    elif 20 <= theta_deg < 32.5:
        return 2160.354 / (np.sin(theta) + (5.7667 * np.cos(theta)))
    elif 32.5 <= theta_deg < 57.5:
        return 400
    elif 57.5 <= theta_deg < 70:
        return 374.6529 / (np.sin(theta) + (0.17341 * np.cos(theta)))
    elif 70 <= theta_deg <= 90.0:
        return 328 / (np.sin(theta) - (0.19012 * np.cos(theta)))
    else:
        return None
    
def washington_nationals(theta_deg):
    """
    Returns the distance "r" in feet to the outfield wall
    at a given angle "theta" in degrees for the Washington Nationals.
    My estimate based on available data.
    """
    theta = np.radians(theta_deg)
    
    if 0.0 <= theta_deg < 13.1:
        return -1192.9 / (np.sin(theta) - (3.56091 * np.cos(theta)))
    elif 13.1 <= theta_deg < 46.5:
        return 1018.837 / (np.sin(theta) + (2.609847 * np.cos(theta)))
    elif 46.5 <= theta_deg < 57.9:
        return 372.8599 / (np.sin(theta) + (0.286983 * np.cos(theta)))
    elif 57.9 <= theta_deg < 59.0:
        return 1089.6378 / (np.sin(theta) + (3.903208 * np.cos(theta)))
    elif 59.0 <= theta_deg < 74.1:
        return 383.87617 / (np.sin(theta) + (0.297133 * np.cos(theta)))
    elif 74.1 <= theta_deg < 74.2:
        return 163.401 / (np.sin(theta) - (1.88975 * np.cos(theta)))
    elif 74.2 <= theta_deg < 76.5:
        return 377.1893 / (np.sin(theta) + (0.261412 * np.cos(theta)))
    elif 76.5 <= theta_deg < 90.0:
        return 336 / (np.sin(theta) - (0.221987 * np.cos(theta)))
    else:

        return None
