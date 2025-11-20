# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import chat_analyze_and_proxy_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.chat_analyze_and_proxy_response import ChatAnalyzeAndProxyResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/safety-gateway-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/safety-gateway-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def analyze_and_proxy(
        self,
        *,
        prompt: str,
        detect_pii: bool | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAnalyzeAndProxyResponse:
        """
        Analyze And Proxy

        Args:
          prompt: The user prompt to validate against safety rules.

          detect_pii: Whether to scan for Personally Identifiable Information (phones, emails).

          model: The target LLM model. Used for specific heuristic adjustments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/chat/completions",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "detect_pii": detect_pii,
                    "model": model,
                },
                chat_analyze_and_proxy_params.ChatAnalyzeAndProxyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatAnalyzeAndProxyResponse,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/safety-gateway-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/safety-gateway-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def analyze_and_proxy(
        self,
        *,
        prompt: str,
        detect_pii: bool | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAnalyzeAndProxyResponse:
        """
        Analyze And Proxy

        Args:
          prompt: The user prompt to validate against safety rules.

          detect_pii: Whether to scan for Personally Identifiable Information (phones, emails).

          model: The target LLM model. Used for specific heuristic adjustments.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/chat/completions",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "detect_pii": detect_pii,
                    "model": model,
                },
                chat_analyze_and_proxy_params.ChatAnalyzeAndProxyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatAnalyzeAndProxyResponse,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.analyze_and_proxy = to_raw_response_wrapper(
            chat.analyze_and_proxy,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.analyze_and_proxy = async_to_raw_response_wrapper(
            chat.analyze_and_proxy,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.analyze_and_proxy = to_streamed_response_wrapper(
            chat.analyze_and_proxy,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.analyze_and_proxy = async_to_streamed_response_wrapper(
            chat.analyze_and_proxy,
        )
