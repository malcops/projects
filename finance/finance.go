package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"github.com/piquette/finance-go/quote"
	"gopkg.in/yaml.v3"
)

func loadYaml(f string) map[string]int {
	file, err := ioutil.ReadFile(f)
	if err != nil {
		log.Fatal(err)
	}
	data := make(map[string]int)
	err1 := yaml.Unmarshal(file, &data)
	if err1 != nil {
		log.Fatal(err1)
	}
	return data
}

func getMarketSummary() string {

	// S&P500, S&P/TSX, CAD/USD, Bitcoin, ETH
	marketInfo := [5]string{"^GSPC", "^GSPTSE", "CADUSD=X", "BTC-CAD", "ETH-CAD"}
	output := fmt.Sprintf("TODAY'S MARKET SUMMARY")
	for _, ticker := range marketInfo {
		dat, err := quote.Get(ticker)
		if err != nil {
			return ""
		}
		output = fmt.Sprintf("%s\n%-10s $%10.2f %-20s", output, ticker, dat.RegularMarketPrice, dat.ShortName)
	}
	return output
}

func getHoldingsSummary(data map[string]int) string {

	total_value := 0.0
	output := "\nHOLDINGS SUMMARY"
	for holding, data := range data {
		dat, err := quote.Get(holding)
		if err != nil {
			return ""
		}
		value := dat.RegularMarketPrice * float64(data)
		output = fmt.Sprintf("%s\n%d shares of %s: $%.2f", output, data, holding, value)

		total_value += value
	}

	res := fmt.Sprintf("Total holdings: $%.2f", total_value)
	return res
}

func main() {
	
	dat := getMarketSummary()
	fmt.Println(dat)

	argsLength := len(os.Args)
	if argsLength > 1 {
		holdings := loadYaml(os.Args[1])
		dat := getHoldingsSummary(holdings)
		fmt.Println(dat)
	}
}
