

```python
import pandas as pd
```


```python
df = pd.read_csv("result_sheet.csv")
```


```python
df.columns
```




    Index(['Roll', 'Name', 'Gender', 'Bangla', 'Math', 'English'], dtype='object')




```python
df["Total"] = df["Bangla"] + df["Math"] + df["English"]
```


```python
df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Roll</th>
      <th>Name</th>
      <th>Gender</th>
      <th>Bangla</th>
      <th>Math</th>
      <th>English</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
      <td>Male</td>
      <td>99</td>
      <td>90</td>
      <td>90</td>
      <td>279</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>B</td>
      <td>Male</td>
      <td>98</td>
      <td>99</td>
      <td>94</td>
      <td>291</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>C</td>
      <td>Female</td>
      <td>97</td>
      <td>93</td>
      <td>99</td>
      <td>289</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>A</td>
      <td>Female</td>
      <td>96</td>
      <td>92</td>
      <td>92</td>
      <td>280</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>B</td>
      <td>Female</td>
      <td>95</td>
      <td>91</td>
      <td>91</td>
      <td>277</td>
    </tr>
  </tbody>
</table>
</div>




```python
ndf = df.sort_values("Total", ascending=False)
```


```python
del df["New Roll"]
```


```python
ndf.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Roll</th>
      <th>Name</th>
      <th>Gender</th>
      <th>Bangla</th>
      <th>Math</th>
      <th>English</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>B</td>
      <td>Male</td>
      <td>98</td>
      <td>99</td>
      <td>94</td>
      <td>291</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>C</td>
      <td>Female</td>
      <td>97</td>
      <td>93</td>
      <td>99</td>
      <td>289</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>A</td>
      <td>Female</td>
      <td>96</td>
      <td>92</td>
      <td>92</td>
      <td>280</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
      <td>Male</td>
      <td>99</td>
      <td>90</td>
      <td>90</td>
      <td>279</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>B</td>
      <td>Female</td>
      <td>95</td>
      <td>91</td>
      <td>91</td>
      <td>277</td>
    </tr>
  </tbody>
</table>
</div>




```python
ndf["New Roll"] = df.index + 1
```


```python
ndf.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Roll</th>
      <th>Name</th>
      <th>Gender</th>
      <th>Bangla</th>
      <th>Math</th>
      <th>English</th>
      <th>Total</th>
      <th>New Roll</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>B</td>
      <td>Male</td>
      <td>98</td>
      <td>99</td>
      <td>94</td>
      <td>291</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>C</td>
      <td>Female</td>
      <td>97</td>
      <td>93</td>
      <td>99</td>
      <td>289</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>A</td>
      <td>Female</td>
      <td>96</td>
      <td>92</td>
      <td>92</td>
      <td>280</td>
      <td>3</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
      <td>Male</td>
      <td>99</td>
      <td>90</td>
      <td>90</td>
      <td>279</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>B</td>
      <td>Female</td>
      <td>95</td>
      <td>91</td>
      <td>91</td>
      <td>277</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>A</td>
      <td>Female</td>
      <td>93</td>
      <td>89</td>
      <td>89</td>
      <td>271</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>B</td>
      <td>Male</td>
      <td>92</td>
      <td>88</td>
      <td>88</td>
      <td>268</td>
      <td>7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>C</td>
      <td>Female</td>
      <td>91</td>
      <td>87</td>
      <td>87</td>
      <td>265</td>
      <td>8</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>B</td>
      <td>Female</td>
      <td>96</td>
      <td>82</td>
      <td>82</td>
      <td>260</td>
      <td>9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>B</td>
      <td>Male</td>
      <td>89</td>
      <td>85</td>
      <td>85</td>
      <td>259</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
#ndf = df[["New Roll", "Name", ]]
```


```python
ndf.rename(columns={"Roll": "Old Roll"})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Old Roll</th>
      <th>Name</th>
      <th>Gender</th>
      <th>Bangla</th>
      <th>Math</th>
      <th>English</th>
      <th>Total</th>
      <th>New Roll</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>B</td>
      <td>Male</td>
      <td>98</td>
      <td>99</td>
      <td>94</td>
      <td>291</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>C</td>
      <td>Female</td>
      <td>97</td>
      <td>93</td>
      <td>99</td>
      <td>289</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>A</td>
      <td>Female</td>
      <td>96</td>
      <td>92</td>
      <td>92</td>
      <td>280</td>
      <td>3</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>A</td>
      <td>Male</td>
      <td>99</td>
      <td>90</td>
      <td>90</td>
      <td>279</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>B</td>
      <td>Female</td>
      <td>95</td>
      <td>91</td>
      <td>91</td>
      <td>277</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>A</td>
      <td>Female</td>
      <td>93</td>
      <td>89</td>
      <td>89</td>
      <td>271</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>B</td>
      <td>Male</td>
      <td>92</td>
      <td>88</td>
      <td>88</td>
      <td>268</td>
      <td>7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>C</td>
      <td>Female</td>
      <td>91</td>
      <td>87</td>
      <td>87</td>
      <td>265</td>
      <td>8</td>
    </tr>
    <tr>
      <th>13</th>
      <td>14</td>
      <td>B</td>
      <td>Female</td>
      <td>96</td>
      <td>82</td>
      <td>82</td>
      <td>260</td>
      <td>9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>B</td>
      <td>Male</td>
      <td>89</td>
      <td>85</td>
      <td>85</td>
      <td>259</td>
      <td>10</td>
    </tr>
    <tr>
      <th>11</th>
      <td>12</td>
      <td>C</td>
      <td>Male</td>
      <td>88</td>
      <td>84</td>
      <td>84</td>
      <td>256</td>
      <td>11</td>
    </tr>
    <tr>
      <th>12</th>
      <td>13</td>
      <td>A</td>
      <td>Female</td>
      <td>87</td>
      <td>83</td>
      <td>83</td>
      <td>253</td>
      <td>12</td>
    </tr>
    <tr>
      <th>14</th>
      <td>15</td>
      <td>C</td>
      <td>Male</td>
      <td>85</td>
      <td>81</td>
      <td>81</td>
      <td>247</td>
      <td>13</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16</td>
      <td>A</td>
      <td>Male</td>
      <td>84</td>
      <td>80</td>
      <td>80</td>
      <td>244</td>
      <td>14</td>
    </tr>
    <tr>
      <th>16</th>
      <td>17</td>
      <td>B</td>
      <td>Male</td>
      <td>83</td>
      <td>79</td>
      <td>79</td>
      <td>241</td>
      <td>15</td>
    </tr>
    <tr>
      <th>17</th>
      <td>18</td>
      <td>C</td>
      <td>Male</td>
      <td>82</td>
      <td>78</td>
      <td>78</td>
      <td>238</td>
      <td>16</td>
    </tr>
    <tr>
      <th>18</th>
      <td>19</td>
      <td>A</td>
      <td>Male</td>
      <td>81</td>
      <td>77</td>
      <td>77</td>
      <td>235</td>
      <td>17</td>
    </tr>
    <tr>
      <th>19</th>
      <td>20</td>
      <td>B</td>
      <td>Male</td>
      <td>80</td>
      <td>76</td>
      <td>76</td>
      <td>232</td>
      <td>18</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>A</td>
      <td>Male</td>
      <td>90</td>
      <td>86</td>
      <td>46</td>
      <td>222</td>
      <td>19</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>C</td>
      <td>Male</td>
      <td>94</td>
      <td>30</td>
      <td>90</td>
      <td>214</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
ndf.to_csv("new_result.csv")
```
