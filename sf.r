library(sf)
shp_data <- read_sf('C:\\Data\\PhD\\Conferences\\GeometryOfRedistricting\\Data\\Wards2017_ED12toED16\\Wards2017_ED12toED16.shp')
fit <- lm(USSREP14 ~ WHITE18+BLACK18+HISPANIC18+ASIAN18+AMINDIAN18+PISLAND18+OTHER18+OTHERMLT18, data=shp_data)
summary(fit) # show results
plot(shp_data["USSREP14"])
gde_15 <- readOGR("C:\\Data\\PhD\\Conferences\\GeometryOfRedistricting\\Data\\Wards2017_ED12toED16\\Wards2017_ED12toED16.shp", layer = "gde-1-1-15")