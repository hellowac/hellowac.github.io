---
comments: true
---

# oauth2学习笔记

## 参考资料

* [理解OAuth 2.0](https://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html) - 阮一峰
* 一、[OAuth 2.0 的一个简单解释](https://www.ruanyifeng.com/blog/2019/04/oauth_design.html) - 阮一峰
* 二、[OAuth 2.0 的四种方式](https://www.ruanyifeng.com/blog/2019/04/oauth-grant-types.html) - 阮一峰
* 三、[GitHub OAuth 第三方登录示例教程](http://www.ruanyifeng.com/blog/2019/04/github-oauth.html) - 阮一峰

* [RFC6749](https://datatracker.ietf.org/doc/html/rfc6749#page-43) - Oauth 2.0 RFC标准

* [RFC6749-中文翻译](https://github.com/jeansfish/RFC6749.zh-cn/blob/master/TableofContents.md) - github仓库

* [RFC7230-7237 - HTTP/1.1](https://github.com/pearzl/HTTP11_chinese) - github仓库
* [HTTP 相关的 RFCs 中英文对照](https://github.com/duoani/HTTP-RFCs.zh-cn) - github仓库 - 推荐

<!-- more -->

## 初识

### 基本流程

![outh验证基本流程](http://www.plantuml.com/plantuml/png/SoWkIImgAStDuIh9BCb9jLB8Bot9CD8pUBcgvyNwngVpTpsRi-RPriRdAxgvk6gUhrdpP4Vdisaxds_U_Npt_1eki6Okg-TJDhzOl_rPNyUpkStMN3NAZdabcOMbgU4PcIMfDKztJNa-PGLCXzMplgLF-wU3b6ziikQoWZ0GMjFpSr9gWEgVTMol0HgySDsBTKlWYfzsjBrixGMgV3bpWZKNYibmnH1PkE8dkvSyx-onHd8xmYLJjZtjs01JK5oINy3ba9gN0WmB0000)

powered by [platuml](https://plantuml.com/zh/activity-diagram-beta)(活动图)

### 密码与令牌

令牌（token）与密码（password）的作用是一样的，都可以进入系统，但是有三点差异。

1. 令牌`是短期的`，到期会自动失效，用户自己无法修改。密码一般长期有效，用户不修改，就不会发生变化。
2. 令牌`可以被数据所有者撤销`，会立即失效。以上例而言，用户可以随时取消第三方系统的令牌。密码一般不允许被他人撤销。
3. 令牌`有权限范围`（scope），比如只能进行读取，不能写入，不能操作。对于网络服务来说，只读令牌就比读写令牌更安全。密码一般是完整权限。

上面这些设计，保证了令牌既可以让**第三方应用获得权限，同时又随时可控，不会危及系统安全**。这就是 `OAuth 2.0` 的3个 `优点`。

## 四种方式

RFC 定义:

!!! info "RFC6749"
    The OAuth 2.0 authorization framework enables a third-party application to obtain limited access to an HTTP service, either on behalf of a resource owner by orchestrating an approval interaction between the resource owner and the HTTP service, or by allowing the third-party application to obtain access on its own behalf.  This specification replaces and obsoletes the OAuth 1.0 protocol described in [RFC 5849](https://datatracker.ietf.org/doc/html/rfc5849).

    翻译:

    OAuth 2.0 授权框架 使 第三方应用程序 能够代表 资源所有者 通过 协调资源所有者 和 HTTP服务之间 的批准交互，或允许第三方应用程序获得对 HTTP 服务的有限访问 以自己的名义获取访问权限。 该规范取代并废弃了 [RFC 5849](https://datatracker.ietf.org/doc/html/rfc5849) 中描述的 OAuth 1.0 协议。

同时 `RFC 6749` 定义了 四种获取令牌的方式

1. 授权码（[authorization-code](https://datatracker.ietf.org/doc/html/rfc6749#page-24)）
2. 隐藏式（[implicit](https://datatracker.ietf.org/doc/html/rfc6749#page-31)）
3. 密码式（[password](https://datatracker.ietf.org/doc/html/rfc6749#page-37)）
4. 客户端凭证（[client credentials](https://datatracker.ietf.org/doc/html/rfc6749#page-40)）

同时该协议还强调：

不管哪一种授权方式，第三方应用申请令牌之前，都必须先到系统备案，说明自己的身份，然后会拿到两个身份识别码：`客户端ID`（client ID）和`客户端密钥`（client secret）。这是为了防止令牌被滥用，没有备案过的第三方应用，是不会拿到令牌的。 参考: [Client Registration](https://datatracker.ietf.org/doc/html/rfc6749#page-13)

### 第一种方式: 授权码 (Authorization Code Grant)

**授权码（`authorization code`）方式，指的是第三方应用先申请一个授权码，然后再用该码获取令牌。** 标准参考: [Authorization Code Grant](https://datatracker.ietf.org/doc/html/rfc6749#page-13)

这种方式是最常用的流程，`安全性`也最高，它适用于那些有`后端`的 `Web应用`。授权码通过前端传送，令牌则是储存在后端，而且所有与资源服务器的通信都在后端完成。这样的前后端分离，可以避免令牌泄漏。

!!! info "RFC6749 - Authorization Code Grant <https://datatracker.ietf.org/doc/html/rfc6749#page-13>"

    原文:

    The authorization code grant type is used to obtain both access tokens and refresh tokens and is optimized for confidential clients. Since this is a redirection-based flow, the client must be capable of interacting with the resource owner's user-agent (typically a web browser) and capable of receiving incoming requests (via redirection) from the authorization server.

    翻译:

    授权代码授予类型用于获取访问令牌和刷新令牌，并针对机密客户端进行了优化。 由于这是基于重定向的流程，因此客户端必须能够与资源所有者的用户代理（通常是 Web 浏览器）交互，并能够从授权服务器接收传入请求（通过重定向）。

#### 流程图

![Oauth2.0授权码验证流程图](../svg/2021-12-07-Oauth2授权码验证流程图.svg)

该流程图包含如下步骤:

!!! info ""

    原文:

    * (A) The client initiates the flow by directing the resource owner's user-agent to the authorization endpoint.  The client includesits client identifier, requested scope, local state, and a redirection URI to which the authorization server will send the user-agent back once access is granted (or denied).
    * (B) The authorization server authenticates the resource owner (via the user-agent) and establishes whether the resource owner grants or denies the client's access request.
    * (C)  Assuming the resource owner grants access, the authorization server redirects the user-agent back to the client using the redirection URI provided earlier (in the request or during client registration).  The redirection URI includes an authorization code and any local state provided by the client earlier.
    * (D)  The client requests an access token from the authorization server's token endpoint by including the authorization code received in the previous step.  When making the request, the client authenticates with the authorization server.  The client includes the redirection URI used to obtain the authorization code for verification.
    * (E)  The authorization server authenticates the client, validates the authorization code, and ensures that the redirection URI received matches the URI used to redirect the client in step (C).  If valid, the authorization server responds back with an access token and, optionally, a refresh token.

    翻译:

    * (A) `客户端`通过将`资源拥有者`的用户代理定向到授权端点来启动流程。 客户端包括其`客户端标识符`、`请求的范围`、`本地状态`和`重定向 URI`，一旦授予（或拒绝）访问权限，`授权服务器`会将用户代理发送回该 `URI`。
    * (B) `授权服务器`验证`资源拥有者`（通过`用户代理`）并确定`资源拥有者`是`授予`还是`拒绝`客户端的`访问请求`。
    * (C) 假设`资源拥有者``授予`访问权限，`授权服务器`使用之前提供的`重定向 URI`（在请求中或客户端注册期间）将用户代理重定向回`客户端`。 `重定向 URI`包括`授权码`和`客户端`之前提供的任何`本地状态`。
    * (D) 客户端通过包含在上一步中收到的`授权码`，从`授权服务器`的令牌端点`请求``访问令牌`。 发出请求时，`客户端`向`授权服务器`进行`身份验证`。 `客户端`包含用于获取通过验证的`授权码`的`重定向 URI`。
    * (E) `授权服务器`对`客户端`进行身份验证，验证`授权码`，并确保收到的`重定向 URI` 与`步骤 (C)` 中用于`重定向客户端的URI` 匹配。 如果有效，`授权服务器`将使用访问令牌和可选的`刷新令牌`进行响应。

概括来说分为4个步骤：

1. 获取授权码
2. 用户允许(或拒绝)授权
3. 携带授权码请求令牌(拒绝授权后结束)
4. 携带令牌请求数据或更新令牌

#### 授权请求

原文参考: [RFC6749](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.1){target="_blank"}

请求示例:

```shell
GET /authorize?response_type=code&client_id=s6BhdRkqt3&state=xyz&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb HTTP/1.1
Host: server.example.com
```

参数:

| 名称          | 必须     | 描述                                                                                                                                                                                                                                               |
| ------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| response_type | 是       | 值必须为 `code`                                                                                                                                                                                                                                    |
| client_id     | 是       | 客户端标识, 参考: [Client Identifier](https://datatracker.ietf.org/doc/html/rfc6749#section-2.2){target="_blank"}                                                                                                                                  |
| redirect_uri  | 否       | 重定向地址, 参考: [Redirection Endpoint](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1.2){target="_blank"}                                                                                                                             |
| scope         | 否       | 范围描述, 参考: [Access Token Scope](https://datatracker.ietf.org/doc/html/rfc6749#section-3.3){target="_blank"}                                                                                                                                   |
| state         | 否(推荐) | 客户端用于维护请求和回调之间的状态的不透明值。 授权服务器在将用户代理重定向回客户端时包含此值。 该参数应该用于防止跨站点请求伪造，参考: [Cross-Site Request Forgery](https://datatracker.ietf.org/doc/html/rfc6749#section-10.12){target="_blank"} |

#### 授权响应

原文参考: [RFC6749](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2){target="_blank"}

响应示例:

```shell
HTTP/1.1 302 Found
Location: https://client.example.com/cb?code=SplxlOBeZQQYbYS6WxSbIA&state=xyz
```

参数:

| 名称  | 必须 | 描述                                                                                                                                                                                                                                                                                        |
| ----- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code  | 是   | 授权服务器生成的授权码。 授权代码必须在发布后不久到期，以降低泄漏风险。 推荐的最长授权代码生命周期为 10 分钟。 客户端不得多次使用授权码。 如果一个授权码被多次使用，授权服务器必须拒绝该请求并且应该撤销（如果可能）之前基于该授权码发出的所有令牌。 授权码绑定到客户端标识符和重定向 URI。 |
| state | 是   | 如果客户端授权请求中存在“state”参数。 从客户端收到的确切值。                                                                                                                                                                                                                                |

#### 授权异常响应

原文参考: [RFC6749](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.1)

响应示例:

```shell
HTTP/1.1 302 Found
Location: https://client.example.com/cb?error=access_denied&state=xyz
```

响应体包含:

| 名称              | 必须 | 描述                                                                                                                                                                                           |
| ----------------- | ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| error             | 是   | 一个单独的 ASCII编码的错误码，可选值: `invalid_request` 、`unauthorized_client` 、`access_denied` 、`unsupported_response_type` 、`invalid_scope` 、`server_error` 、`temporarily_unavailable` |
| error_description | 可选 | 可读的错误描述，用于协助客户端开发人员了解发生的错误。                                                                                                                                         |
| error_uri         | 可选 | 可读的网页错误详细描述，用于向客户端提供开发人员提供有关错误的其他信息。                                                                                                                       |
| state             | 可选 | 如果客户端请求存在`state`参数，并且被服务器收到。                                                                                                                                              |

#### 访问令牌请求

原文参考: [RFC6749](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.1)

请求示例:

```shell
POST /token HTTP/1.1
Host: server.example.com
Authorization: Basic czZCaGRSa3F0MzpnWDFmQmF0M2JW
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&code=SplxlOBeZQQYbYS6WxSbIA
&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb
```

请求体包含:

| 名称         | 必须 | 描述                                                             |
| ------------ | ---- | ---------------------------------------------------------------- |
| grant_type   | 是   | 值必须是 `authorization_code`                                    |
| code         | 是   | 从授权服务器收到的授权码。                                       |
| redirect_uri | 是   | 如果`redirect_uri`参数包含在`授权请求`中，并且它们的值必须相同。 |
| client_id    | 是   | 如果客户端没有使用授权服务器进行身份验证时提供。                 |

#### 访问令牌响应

原文参考: [RFC6749](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1.2.1)

响应示例:

```shell
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "access_token":"2YotnFZFEjr1zCsicMWpAA",
  "token_type":"example",
  "expires_in":3600,
  "refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA",
  "example_parameter":"example_value"
}
```

请求体包含:

| 名称          | 必须     | 描述                                                                                                                                                       |
| ------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access_token  | 是       | 授权服务器颁发的访问令牌。                                                                                                                                 |
| token_type    | 是       | 发行的令牌类型，值不区分大小写。参考:  [Access Token Types](https://datatracker.ietf.org/doc/html/rfc6749#section-7.1)                                     |
| expires_in    | 是(推荐) | 访问令牌的生命周期（以秒为单位）。 例如，值“3600”表示访问令牌将在响应生成后的一小时内到期。 如果省略，授权服务器应该通过其他方式提供过期时间或记录默认值。 |
| refresh_token | 是       | 刷新令牌，可使用于相同授权的获取新的访问令牌。 参考: [Refreshing an Access Token](https://datatracker.ietf.org/doc/html/rfc6749#section-6)                 |
| scope         | 可选     | 如果与客户要求的范围相同； 否则，需要。 参考: [Access Token Scope](https://datatracker.ietf.org/doc/html/rfc6749#section-3.3)                              |

#### 访问令牌异常响应

原文参考: [Error Response](https://datatracker.ietf.org/doc/html/rfc6749#section-5.1)

响应示例:

```shell
HTTP/1.1 400 Bad Request
Content-Type: application/json;charset=UTF-8
Cache-Control: no-store
Pragma: no-cache

{
  "error":"invalid_request"
}
```

响应体包含:

| 名称              | 必须 | 描述                                                                                                                                                              |
| ----------------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| error             | 是   | 一个单独的 ASCII编码的错误码，可选值: `invalid_request` 、`invalid_client` 、`invalid_grant` 、`unauthorized_client` 、`unsupported_grant_type` 、`invalid_scope` |
| error_description | 可选 | 可读的错误描述，用于协助客户端开发人员了解发生的错误。                                                                                                            |
| error_uri         | 可选 | 可读的网页错误详细描述，用于向客户端提供开发人员提供有关错误的其他信息。                                                                                          |
| state             | 可选 | 如果客户端请求存在`state`参数，并且被服务器收到。                                                                                                                 |

<https://www.ruanyifeng.com/blog/2019/04/oauth-grant-types.html>{target="_blank"}

### 第二种方式: 隐藏式 (Implicit Grant)

有些 Web 应用是纯前端应用，没有后端。这时就不能用上面的方式了，必须将令牌储存在前端。`RFC 6749` 就规定了第二种方式，允许直接向前端颁发令牌。这种方式没有授权码这个中间步骤，所以称为（授权码）"隐藏式"（`implicit`）。

!!! info "@RFC6749 - Authorization Code Grant <https://datatracker.ietf.org/doc/html/rfc6749#page-13>{target="_blank"}"

    原文:

    The implicit grant type is used to obtain access tokens (it does notsupport the issuance of refresh tokens) and is optimized for publicclients known to operate a particular redirection URI.  These clientsare typically implemented in a browser using a scripting languagesuch as JavaScript.

    Since this is a redirection-based flow, the client must be capable ofinteracting with the resource owner's user-agent (typically a webbrowser) and capable of receiving incoming requests (via redirection)from the authorization server.

    Unlike the authorization code grant type, in which the client makesseparate requests for authorization and for an access token, theclient receives the access token as the result of the authorizationrequest.

    The implicit grant type does not include client authentication, andrelies on the presence of the resource owner and the registration ofthe redirection URI.  Because the access token is encoded into theredirection URI, it may be exposed to the resource owner and otherapplications residing on the same device.

    翻译:

    隐式授权类型用于获取访问令牌（它不支持发布刷新令牌），并针对已知操作特定重定向 URI 的公共客户端进行了优化。 这些客户端通常使用 JavaScript 等脚本语言在浏览器中实现。

    由于这是基于重定向的流程，因此客户端必须能够与资源所有者的用户代理（通常是 Web 浏览器）交互，并能够从授权服务器接收传入请求（通过重定向）。

    与客户端发出单独的授权请求和访问令牌请求的授权代码授予类型不同，客户端接收访问令牌作为授权请求的结果。

    隐式授权类型不包括客户端身份验证，并且依赖于资源所有者的存在和重定向 URI 的注册。 由于访问令牌被编码到重定向 URI 中，因此它可能会暴露给资源所有者和驻留在同一设备上的其他应用程序。

#### 流程图

![Oauth2.0隐藏式验证流程图](../svg/2021-12-08-oauth2隐藏式授权流程图.svg)

该流程图包含如下步骤:

原文:

* (A)  The client initiates the flow by directing the resource owner'suser-agent to the authorization endpoint.  The client includesits client identifier, requested scope, local state, and aredirection URI to which the authorization server will send theuser-agent back once access is granted (or denied).
* (B)  The authorization server authenticates the resource owner (viathe user-agent) and establishes whether the resource ownergrants or denies the client's access request.
* (C)  Assuming the resource owner grants access, the authorizationserver redirects the user-agent back to the client using theredirection URI provided earlier.  The redirection URI includesthe access token in the URI fragment.
* (D)  The user-agent follows the redirection instructions by making arequest to the web-hosted client resource (which does notinclude the fragment per [RFC2616](https://datatracker.ietf.org/doc/html/rfc2616)).  The user-agent retains thefragment information locally.
* (E)  The web-hosted client resource returns a web page (typically anHTML document with an embedded script) capable of accessing thefull redirection URI including the fragment retained by theuser-agent, and extracting the access token (and otherparameters) contained in the fragment.
* (F)  The user-agent executes the script provided by the web-hostedclient resource locally, which extracts the access token.
* (G)  The user-agent passes the access token to the client.

翻译:

* (A) 客户端通过将资源所有者的用户代理定向到授权端点来启动流程。 客户端包括其客户端标识符、请求的范围、本地状态以及授权服务器将在访问被授予（或拒绝）后将用户代理发送回的方向 URI。
* (B) 授权服务器验证资源所有者（通过用户代理）并确定资源所有者是授予还是拒绝客户端的访问请求。
* (C) 假设资源所有者授予访问权限，授权服务器使用之前提供的重定向 URI 将用户代理重定向回客户端。 重定向 URI 包括 URI 片段中的访问令牌。
* (D) 用户代理通过向 Web 托管的客户端资源（不包括每个 [RFC2616](https://datatracker.ietf.org/doc/html/rfc2616) 的片段）发出请求来遵循重定向指令。 用户代理在本地保留片段信息。
* (E) `授权服务器`对`客户端`进行身份验证，验证`授权码`，并确保收到的`重定向 URI` 与`步骤 (C)` 中用于`重定向客户端的URI` 匹配。 如果有效，`授权服务器`将使用访问令牌和可选的`刷新令牌`进行响应。
* (F) 用户代理在本地执行由 Web 托管客户端资源提供的脚本，该脚本提取访问令牌。
* (G) 用户代理将访问令牌传递给客户端。

#### 授权请求

原文参考: [RFC6749](https://datatracker.ietf.org/doc/html/rfc6749#section-4.2.1)

请求示例:

```shell
GET /authorize?response_type=token&client_id=s6BhdRkqt3&state=xyz&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb HTTP/1.1
Host: server.example.com
```

参数:

| 名称          | 必须     | 描述                                                                                                                                                                                                                              |
| ------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| response_type | 是       | 值必须为 `token`                                                                                                                                                                                                                  |
| client_id     | 是       | 客户端标识, 参考: [Client Identifier](https://datatracker.ietf.org/doc/html/rfc6749#section-2.2)                                                                                                                                  |
| redirect_uri  | 否       | 重定向地址, 参考: [Redirection Endpoint](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1.2)                                                                                                                             |
| scope         | 否       | 范围描述, 参考: [Access Token Scope](https://datatracker.ietf.org/doc/html/rfc6749#section-3.3)                                                                                                                                   |
| state         | 否(推荐) | 客户端用于维护请求和回调之间的状态的不透明值。 授权服务器在将用户代理重定向回客户端时包含此值。 该参数应该用于防止跨站点请求伪造，参考: [Cross-Site Request Forgery](https://datatracker.ietf.org/doc/html/rfc6749#section-10.12) |

#### 请求令牌响应

原文参考: [RFC6749 - 4.2.2](https://datatracker.ietf.org/doc/html/rfc6749#section-4.2.2)

请求示例:

```shell
GET /authorize?response_type=token&client_id=s6BhdRkqt3&state=xyz&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb HTTP/1.1
Host: server.example.com
```

参数:

| 名称         | 必须           | 描述                                                                                                                                                       |
| ------------ | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access_token | 是             | 授权服务器颁发的访问令牌。                                                                                                                                 |
| token_type   | 是             | 发行的令牌类型，值不区分大小写。 参考: [Client Identifier](https://datatracker.ietf.org/doc/html/rfc6749#section-7.1)                                      |
| expires_in   | 可选(推荐返回) | 访问令牌的生命周期（以秒为单位）。 例如，值“3600”表示访问令牌将在响应生成后的一小时内到期。 如果省略，授权服务器应该通过其他方式提供过期时间或记录默认值。 |
| scope        | 可选           | 如果与客户端请求的范围相同，则必须返回。 参考: [Access Token Scope](https://datatracker.ietf.org/doc/html/rfc6749#section-3.3)                             |
| state        | 是(推荐)       | 如果客户端授权请求中存在“状态”参数。 从客户端收到的确切值。                                                                                                |

授权服务器不得发出刷新令牌。

#### 错误响应

原文参考: [RFC6749 - 4.2.2.1](https://datatracker.ietf.org/doc/html/rfc6749#section-4.2.2.1)

响应示例:

```shell
HTTP/1.1 302 Found
Location: https://client.example.com/cb#error=access_denied&state=xyz
```

响应体包含:

| 名称              | 必须 | 描述                                                                                                                                                                                           |
| ----------------- | ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| error             | 是   | 一个单独的 ASCII编码的错误码，可选值: `invalid_request` 、`unauthorized_client` 、`access_denied` 、`unsupported_response_type` 、`invalid_scope` 、`server_error` 、`temporarily_unavailable` |
| error_description | 可选 | 可读的错误描述，用于协助客户端开发人员了解发生的错误。                                                                                                                                         |
| error_uri         | 可选 | 可读的网页错误详细描述，用于向客户端提供开发人员提供有关错误的其他信息。                                                                                                                       |
| state             | 可选 | 如果客户端请求存在`state`参数，并且被服务器收到。                                                                                                                                              |

## 第三方示例

<http://www.ruanyifeng.com/blog/2019/04/github-oauth.html>

## 理解oauth 2.0

<https://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html>
