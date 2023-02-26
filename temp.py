from pyquery import PyQuery

html = """
<li class="chapter">
    <h2>A3. <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E8%AE%BE%E7%BD%AE%E4%B8%8E%E9%85%8D%E7%BD%AE">附录 C: Git 命令</a></h2>
      <ol>
            <li>
              A3.1
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E8%AE%BE%E7%BD%AE%E4%B8%8E%E9%85%8D%E7%BD%AE">设置与配置</a>
            </li>
            <li>
              A3.2
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E8%8E%B7%E5%8F%96%E4%B8%8E%E5%88%9B%E5%BB%BA%E9%A1%B9%E7%9B%AE">获取与创建项目</a>
            </li>
            <li>
              A3.3
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E5%BF%AB%E7%85%A7%E5%9F%BA%E7%A1%80">快照基础</a>
            </li>
            <li>
              A3.4
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E5%88%86%E6%94%AF%E4%B8%8E%E5%90%88%E5%B9%B6">分支与合并</a>
            </li>
            <li>
              A3.5
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E9%A1%B9%E7%9B%AE%E5%88%86%E4%BA%AB%E4%B8%8E%E6%9B%B4%E6%96%B0">项目分享与更新</a>
            </li>
            <li>
              A3.6
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E6%A3%80%E6%9F%A5%E4%B8%8E%E6%AF%94%E8%BE%83">检查与比较</a>
            </li>
            <li>
              A3.7
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E8%B0%83%E8%AF%95">调试</a>
            </li>
            <li>
              A3.8
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E8%A1%A5%E4%B8%81">补丁</a>
            </li>
            <li>
              A3.9
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E9%82%AE%E4%BB%B6">邮件</a>
            </li>
            <li>
              A3.10
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E5%A4%96%E9%83%A8%E7%B3%BB%E7%BB%9F">外部系统</a>
            </li>
            <li>
              A3.11
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E7%AE%A1%E7%90%86">管理</a>
            </li>
            <li>
              A3.12
              <a href="/book/zh/v2/%E9%99%84%E5%BD%95-C%3A-Git-%E5%91%BD%E4%BB%A4-%E5%BA%95%E5%B1%82%E5%91%BD%E4%BB%A4">底层命令</a>
            </li>
      </ol>
    </li>
"""

pq = PyQuery(html)

for h2 in pq("h2").items():
    title = h2.text()
    a = h2("a").eq(0)
    a_text = a.text()
    a_href = a.attr("href")
    link = f"[{a_text}](https://git-scm.com{a_href})" + '{target="_blank"}'

    line = "## " + title.replace(a_text, link)
    print(line)

print("\n")
for li in pq("ol > li").items():
    title = li.text()
    a = li("a").eq(0)
    a_text = a.text()
    a_href = a.attr("href")
    link = f"[{a_text}](https://git-scm.com{a_href})" + '{target="_blank"}'

    line = "- " + title.replace(a_text, link)
    print(line)

# print(pa.text())
