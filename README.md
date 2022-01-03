# 免责申明 DISCLAIMER

THIS SOFTWARE SHOULD NEVER BE USED IN PUBLIC GAMING, AND SHOULD NEVER BE USED WITHOUT THE PERMISSION OF OTHER GAMERS. THIS SOFTWARE IS ONLY A TECHNICAL VALIDATION, BUT NOT A TOOL OR HELPER. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

本软件不应该被用于公开游戏，亦不得在未获得其他玩家同意的情况下使用。本软件只是一个技术验证而非助手或者工具。在任何情况下，作者或版权持有人都不对任何索赔、损害或其他责任负责，无论这些追责来自合同、侵权或其它行为中，还是产生于、源于或有关于本软件以及本软件的使用或其它处置。

# 简介

通过 CV 来对 Stick Fight: The Game 实现敌人自动追踪

# `hsv_calc.py`

## 简介

计算除了纯白区域以外的 `HSV` 色彩空间的范围，给出 `h_min`, `h_max`, `s_min`, `s_max`, `v_min`, `v_max`

## 使用

替换 `'./imgs/yellow-3.png'` 未需要处理的图片。

```bash
python3 hsv_calc.py
```

# `loop_demo.py`

## 简介

闭环流程如下：

* 对窗体进行截图
* 根据截图 filter 出固定颜色的色彩范围
* 计算出 mask 的重心
* 根据窗体位置计算出鼠标的绝对坐标
* 操作鼠标自瞄

效果为 50 fps 左右

## 使用

现在只对黄色小人做了追踪，通过 HSV 的 upper and lower color, 具体设置为：

```python
lower_yellow = (20, 198, 219)
upper_yellow = (24, 209, 249)
```

还需要设置系统的 DPI 缩放比例 (这里是 125%)：

```python
dpi_scale = 1.25
```

```
python3 loop_demo.py
```
