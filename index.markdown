---
layout: default
---

<div>
  <ul class="listing">
  {% for post in site.posts limit: 15 %}
  <article class="content">
    <section class="title">
      <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    </section>
    <section class="meta">
    <span class="time">
      <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
    </span>
    {% if post.tags %}
    <span class="tags">
      {% for tag in post.tags %}
      <a href="/tags.html#{{ tag }}" title="{{ tag }}">#{{ tag }}</a>
      {% endfor %}
    </span>
    {% endif %}
    </section>
  </article>
  {% endfor %}
  </ul>
  <div class="sidebar">
        <iframe src="http://githubbadge.appspot.com/badge/freetstar?s=1&a=0" style="border: 0;height: 130px;width: 200px;overflow: hidden;"></iframe>
        <a href="http://firefox.com.cn/"><img border="0" alt="Spread Firefox Affiliate Button" src="http://firefox.com.cn/static/images/about/spread/110-30orange.png"></a>
        <script type="text/javascript" src="http://www.douban.com/service/badge/freetstar/?show=collection&amp;select=favorite&amp;n=10&amp;columns=2" ></script> 
        <script type="text/javascript"><!--
        google_ad_client = "ca-pub-7623790890973408";
        google_ad_slot = "7024979808";
        google_ad_width = 200;
        google_ad_height = 200;
        //-->
        </script>
        <script type="text/javascript"
        src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
        </script>
  </div>

  <div class="center">
      <a href="/archive.html" class="circle-wrapper">
      <div class="circle">&nbsp;</div>
      <div class="circle">&nbsp;</div>
      <div class="circle">&nbsp;</div>
      </a>
  </div>
</div>
