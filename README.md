# Major Events and Global Markets: a cross-country, cross-industry event study

How do major macro shocks reprice stocks across industries and across
countries? This study applies the event-study method (CAPM market model,
abnormal and cumulative abnormal returns) to **11 industries** under **5 major
events**, comparing the UK, US, and Chinese markets.

**Course:** Event study project, School of Economics and Management, Tsinghua
University, December 2024. **Advisor:** Prof. Sun Jing.
**Authors:** Zhu Hongyi, Marco Ortiz Togashi.

## The design

**Five events** (event date used as day 0):

| Event | Date |
|---|---|
| Global Financial Crisis (Lehman) | 2008-09-15 |
| Brexit Referendum | 2016-06-23 |
| Covid-19 lockdown in China | 2020-01-23 |
| Russia-Ukraine war | 2022-02-24 |
| Trump re-election | 2024-11-06 |

**Eleven industries:** Agriculture & Food, Automotive, Defense & Aerospace,
Energy & Utilities, Finance & Insurance, Healthcare & Pharmaceuticals,
Manufacturing & Industrial Goods, Real Estate & Construction, Retail &
Consumer Goods, Technology & Telecommunications, Transportation &
Infrastructure.

For each industry-event cell, an industry return series is regressed on its
market index over a pre-event estimation window to fit a CAPM market model.
Expected returns are projected into a 30-day event window, the abnormal return
is actual minus expected, and abnormal returns accumulate into a CAR path. OLS
summaries (alpha, beta, R-squared, p-value) quantify each fit, and abnormal
returns are compared across industries per event.

## Findings

Industries diverge sharply in their sensitivity to events. Defense &
aerospace, technology, and healthcare behaved as **safe havens** during
geopolitical conflict and the public-health shock, while energy and
manufacturing were **pressured** through supply-chain disruption and demand
swings. The study reads these differences through policy-transmission,
market-efficiency, and industry-vulnerability lenses, with cross-industry
comparison per event (see `figures/`).

## Repository layout

```
src/                     analysis pipeline (run in this order)
  split_by_events.py                 split combined returns into per-event files
  expected_return_calculation.py     CAPM expected returns per industry-event
  ar_calculation.py                  abnormal return = industry - expected
  event_analysis_expected_return.py  expected-return event-study step
  event_analysis_ar_car.py           AR / CAR construction and plots
  event_analysis_ols.py              market-model OLS per industry-event
results/
  ols/                   55 OLS summaries (11 industries x 5 events): alpha, beta, R^2, p
  expected_returns/      55 expected-return series (CAPM projections)
  abnormal_returns/      55 abnormal-return series (industry, market, expected, AR)
  ar_car_results.csv     per-company CAR over each event window
  industry_averages.csv, industry_30day_averages.csv,
  industry_event_30day_returns_cleaned.csv   aggregated industry return panels
figures/                 5 cross-industry AR comparison plots (one per event)
```

## Reproduce

```bash
pip install -r requirements.txt
# The scripts run in the order listed above. Note: they were written with
# absolute Windows paths pointing at the original author's machine
# (for example C:\Users\...\Escritorio\...). Adjust the folder paths at the
# top of each script to your local checkout before running.
```

## Data

Stock and index prices were pulled from Yahoo Finance for the UK, US, and
Chinese markets. **Raw price data is not committed** (Yahoo Finance data is
not redistributable): only derived series and statistics are stored here, the
CAPM expected returns, the abnormal-return series, the OLS summaries, the
aggregated industry return panels, and the comparison figures. None of the
committed CSVs contain raw OHLC quotes; they hold return series (percentage
changes) and regression outputs only.

## Notes and limitations

- The analysis scripts carry hard-coded absolute paths from the original
  working directory; they are kept verbatim as a record of what was run and
  need repointing to reproduce.
- `Event Analysis.py` from the original working folder is **not** part of this
  project (it is an unrelated app-comparison script that happened to share the
  name) and is intentionally excluded.
- Estimation and event windows are short, so single-cell significance should
  be read alongside the cross-industry comparison rather than in isolation.

## License

Code is released under the MIT License (see `LICENSE`). The accompanying
written report remains the intellectual work of the two authors and is not
included in this repository.
