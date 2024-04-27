# Earthquake checker 
## 一個讓你可以用 Command line 快速確認剛剛有沒有地震的工具
近期因為地震太多，工作的時候總是有同事問剛剛是不是有地震。在這個時候可以輕鬆的用 Command line 去確認有沒有地震，不用打開網頁視窗，是一個雞肋的小工具。這個工具能幫你查詢中央氣象署的資料，並將處理後的資料輸出在 terminal 上面，免取上網查詢的動作

## Get started
earthquake-check requires Python 3.6+ along with the requests and pydantic.
1. 安裝套件
    ```
    pip install earthquake-check
    ```
2. 檢視最近 1 小時內是否有地震
    ```
    equake check
    ```
    ![image](https://github.com/ChickenBenny/equake-check/assets/96862600/8439637c-2d24-4a87-b835-a5156ef9d313)

    **預設是檢查一小時內，可以使用 `--hour=${希望的小時}`**
3. 顯示近期地震的資訊
    ```
    equake show
    ```
    ![image](https://github.com/ChickenBenny/equake-check/assets/96862600/e248fe55-43ee-4cc6-9349-789cc51d2d68)
    **預設是五筆，可以使用 `--hour=${希望的小時}`**

## 結語
總之這就是一個雞肋的小套件，大家可以載來玩玩看。阿如果中央氣象署的資料改了，可能也不會繼續維護。
![image](https://github.com/ChickenBenny/equake-check/assets/96862600/a4d3e791-b597-4377-8265-7ee9ef3ef558)
