# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdAccountAdVolume(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdAccountAdVolume, self).__init__()
        self._isAdAccountAdVolume = True
        self._api = api

    class Field(AbstractObject.Field):
        actor_id = 'actor_id'
        actor_name = 'actor_name'
        ad_limit_scope_business = 'ad_limit_scope_business'
        ad_limit_scope_business_manager_id = 'ad_limit_scope_business_manager_id'
        ad_limit_set_by_page_admin = 'ad_limit_set_by_page_admin'
        ads_running_or_in_review_count = 'ads_running_or_in_review_count'
        ads_running_or_in_review_count_subject_to_limit_set_by_page = 'ads_running_or_in_review_count_subject_to_limit_set_by_page'
        current_account_ads_running_or_in_review_count = 'current_account_ads_running_or_in_review_count'
        future_limit_activation_date = 'future_limit_activation_date'
        future_limit_on_ads_running_or_in_review = 'future_limit_on_ads_running_or_in_review'
        limit_on_ads_running_or_in_review = 'limit_on_ads_running_or_in_review'
        recommendations = 'recommendations'

    class RecommendationType:
        aac_creation_package = 'AAC_CREATION_PACKAGE'
        ab_test = 'AB_TEST'
        account_error = 'ACCOUNT_ERROR'
        account_needs_credit = 'ACCOUNT_NEEDS_CREDIT'
        account_spend_limit = 'ACCOUNT_SPEND_LIMIT'
        account_spend_limit_duplication = 'ACCOUNT_SPEND_LIMIT_DUPLICATION'
        aco_toggle = 'ACO_TOGGLE'
        ads_reporting = 'ADS_REPORTING'
        ads_status = 'ADS_STATUS'
        advanced_campaign_budget = 'ADVANCED_CAMPAIGN_BUDGET'
        advantage_app_campaign = 'ADVANTAGE_APP_CAMPAIGN'
        advantage_campaign_budget_duplication = 'ADVANTAGE_CAMPAIGN_BUDGET_DUPLICATION'
        advantage_custom_audience = 'ADVANTAGE_CUSTOM_AUDIENCE'
        advantage_custom_audience_duplication = 'ADVANTAGE_CUSTOM_AUDIENCE_DUPLICATION'
        advantage_custom_audience_upsell = 'ADVANTAGE_CUSTOM_AUDIENCE_UPSELL'
        advantage_detailed_targeting = 'ADVANTAGE_DETAILED_TARGETING'
        advantage_lookalike_audience = 'ADVANTAGE_LOOKALIKE_AUDIENCE'
        advantage_lookalike_duplication = 'ADVANTAGE_LOOKALIKE_DUPLICATION'
        advantage_plus_app_campaign = 'ADVANTAGE_PLUS_APP_CAMPAIGN'
        advantage_plus_app_campaign_precreate = 'ADVANTAGE_PLUS_APP_CAMPAIGN_PRECREATE'
        advantage_plus_audience = 'ADVANTAGE_PLUS_AUDIENCE'
        advantage_plus_audience_duplication = 'ADVANTAGE_PLUS_AUDIENCE_DUPLICATION'
        advantage_plus_audience_friction = 'ADVANTAGE_PLUS_AUDIENCE_FRICTION'
        advantage_plus_audience_toggle = 'ADVANTAGE_PLUS_AUDIENCE_TOGGLE'
        advantage_plus_campaign_budget = 'ADVANTAGE_PLUS_CAMPAIGN_BUDGET'
        advantage_plus_catalog_ads = 'ADVANTAGE_PLUS_CATALOG_ADS'
        advantage_plus_creative = 'ADVANTAGE_PLUS_CREATIVE'
        advantage_plus_creative_catalog = 'ADVANTAGE_PLUS_CREATIVE_CATALOG'
        advantage_plus_creative_se = 'ADVANTAGE_PLUS_CREATIVE_SE'
        advantage_plus_placements_duplication = 'ADVANTAGE_PLUS_PLACEMENTS_DUPLICATION'
        advantage_plus_placements_friction = 'ADVANTAGE_PLUS_PLACEMENTS_FRICTION'
        advantage_plus_placements_v2_duplication = 'ADVANTAGE_PLUS_PLACEMENTS_V2_DUPLICATION'
        advantage_shopping_campaign = 'ADVANTAGE_SHOPPING_CAMPAIGN'
        advantage_shopping_campaign_fragmentation = 'ADVANTAGE_SHOPPING_CAMPAIGN_FRAGMENTATION'
        ad_lift_recall_goal = 'AD_LIFT_RECALL_GOAL'
        ad_lift_recall_goal_precreate = 'AD_LIFT_RECALL_GOAL_PRECREATE'
        ad_lift_recall_optimization_goal = 'AD_LIFT_RECALL_OPTIMIZATION_GOAL'
        ad_objective = 'AD_OBJECTIVE'
        aem_v2_ineligible = 'AEM_V2_INELIGIBLE'
        aggregated_bid_limited = 'AGGREGATED_BID_LIMITED'
        aggregated_budget_limited = 'AGGREGATED_BUDGET_LIMITED'
        aggregated_cost_limited = 'AGGREGATED_COST_LIMITED'
        aplus_c_catalog_duplication = 'APLUS_C_CATALOG_DUPLICATION'
        app_aem_v2_installation_promotion = 'APP_AEM_V2_INSTALLATION_PROMOTION'
        app_engaged_view_conversions_duplication = 'APP_ENGAGED_VIEW_CONVERSIONS_DUPLICATION'
        asc_budget_optimization = 'ASC_BUDGET_OPTIMIZATION'
        asc_creation_package = 'ASC_CREATION_PACKAGE'
        asc_fragmentation_v2 = 'ASC_FRAGMENTATION_V2'
        asc_precreate = 'ASC_PRECREATE'
        aspect_ratio = 'ASPECT_RATIO'
        atleast_6_placements = 'ATLEAST_6_PLACEMENTS'
        auction_overlap = 'AUCTION_OVERLAP'
        auction_overlap_consolidation = 'AUCTION_OVERLAP_CONSOLIDATION'
        audience_expansion = 'AUDIENCE_EXPANSION'
        audience_expansion_georadius = 'AUDIENCE_EXPANSION_GEORADIUS'
        audience_expansion_lookalike = 'AUDIENCE_EXPANSION_LOOKALIKE'
        audience_expansion_retargeting = 'AUDIENCE_EXPANSION_RETARGETING'
        audience_learning_limited = 'AUDIENCE_LEARNING_LIMITED'
        autoflow_opt_in = 'AUTOFLOW_OPT_IN'
        autoflow_opt_in_fallback_duplication_flow = 'AUTOFLOW_OPT_IN_FALLBACK_DUPLICATION_FLOW'
        autoflow_opt_in_v2 = 'AUTOFLOW_OPT_IN_V2'
        automatic_placements = 'AUTOMATIC_PLACEMENTS'
        automatic_placements_v2 = 'AUTOMATIC_PLACEMENTS_V2'
        auto_bid = 'AUTO_BID'
        background_generation = 'BACKGROUND_GENERATION'
        blended_ads = 'BLENDED_ADS'
        blended_ads_duplication = 'BLENDED_ADS_DUPLICATION'
        blended_ads_for_shops_ads_duplication = 'BLENDED_ADS_FOR_SHOPS_ADS_DUPLICATION'
        broad_targeting = 'BROAD_TARGETING'
        budget_limited = 'BUDGET_LIMITED'
        capi = 'CAPI'
        capi_crm_guidance = 'CAPI_CRM_GUIDANCE'
        capi_performance_match_key = 'CAPI_PERFORMANCE_MATCH_KEY'
        capi_performance_match_key_v2 = 'CAPI_PERFORMANCE_MATCH_KEY_V2'
        cash_rewards_opt_in = 'CASH_REWARDS_OPT_IN'
        catalog_match_rate = 'CATALOG_MATCH_RATE'
        commerce_shops_ads_duplication = 'COMMERCE_SHOPS_ADS_DUPLICATION'
        connected_sources = 'CONNECTED_SOURCES'
        connected_sources_duplication = 'CONNECTED_SOURCES_DUPLICATION'
        connect_facebook_page_to_instagram = 'CONNECT_FACEBOOK_PAGE_TO_INSTAGRAM'
        connect_facebook_page_to_whatsapp = 'CONNECT_FACEBOOK_PAGE_TO_WHATSAPP'
        conversion_lead_ads = 'CONVERSION_LEAD_ADS'
        cost_goal = 'COST_GOAL'
        cost_goal_budget_limited = 'COST_GOAL_BUDGET_LIMITED'
        cost_goal_cpa_limited = 'COST_GOAL_CPA_LIMITED'
        cost_per_result = 'COST_PER_RESULT'
        creation_package_upgrade_to_asc = 'CREATION_PACKAGE_UPGRADE_TO_ASC'
        creation_package_upgrade_to_ctx = 'CREATION_PACKAGE_UPGRADE_TO_CTX'
        creation_package_upgrade_to_tla = 'CREATION_PACKAGE_UPGRADE_TO_TLA'
        creation_package_upgrade_to_tmc = 'CREATION_PACKAGE_UPGRADE_TO_TMC'
        creative_badge = 'CREATIVE_BADGE'
        creative_diversity = 'CREATIVE_DIVERSITY'
        creative_fatigue = 'CREATIVE_FATIGUE'
        creative_fatigue_duplication = 'CREATIVE_FATIGUE_DUPLICATION'
        creative_fatigue_hourly = 'CREATIVE_FATIGUE_HOURLY'
        creative_limited = 'CREATIVE_LIMITED'
        creative_limited_duplication = 'CREATIVE_LIMITED_DUPLICATION'
        creative_limited_hourly = 'CREATIVE_LIMITED_HOURLY'
        creator_ads_pa_conversion = 'CREATOR_ADS_PA_CONVERSION'
        cta = 'CTA'
        ctx_budget_optimization = 'CTX_BUDGET_OPTIMIZATION'
        ctx_creation_package = 'CTX_CREATION_PACKAGE'
        ctx_cta_upgrade_in_duplication = 'CTX_CTA_UPGRADE_IN_DUPLICATION'
        ctx_ctmpo_upgrade = 'CTX_CTMPO_UPGRADE'
        ctx_guidance = 'CTX_GUIDANCE'
        ctx_precreate = 'CTX_PRECREATE'
        da_advantage_plus_creative_info_labels = 'DA_ADVANTAGE_PLUS_CREATIVE_INFO_LABELS'
        da_duplication_product_tags = 'DA_DUPLICATION_PRODUCT_TAGS'
        dead_link = 'DEAD_LINK'
        defragmentation_acb = 'DEFRAGMENTATION_ACB'
        defragmentation_acb_duplication = 'DEFRAGMENTATION_ACB_DUPLICATION'
        delivery_error = 'DELIVERY_ERROR'
        delivery_warning = 'DELIVERY_WARNING'
        dynamic_advantage_campaign_budget = 'DYNAMIC_ADVANTAGE_CAMPAIGN_BUDGET'
        ecosystem_bid_reduce_l1_cardinality = 'ECOSYSTEM_BID_REDUCE_L1_CARDINALITY'
        engaged_view_conversions_creation = 'ENGAGED_VIEW_CONVERSIONS_CREATION'
        evc_app_duplication_upgrade = 'EVC_APP_DUPLICATION_UPGRADE'
        evc_web_duplication_upgrade = 'EVC_WEB_DUPLICATION_UPGRADE'
        fragmentation = 'FRAGMENTATION'
        fragmentation_resolution_update = 'FRAGMENTATION_RESOLUTION_UPDATE'
        fragmentation_v2 = 'FRAGMENTATION_V2'
        generative_uncrop_duplication = 'GENERATIVE_UNCROP_DUPLICATION'
        ges_test = 'GES_TEST'
        guidance_center_code_gen = 'GUIDANCE_CENTER_CODE_GEN'
        heuristic_default_duration = 'HEURISTIC_DEFAULT_DURATION'
        high_cost = 'HIGH_COST'
        historical_benchmark = 'HISTORICAL_BENCHMARK'
        ig_multi_ads = 'IG_MULTI_ADS'
        ig_surfaces_manual_placements = 'IG_SURFACES_MANUAL_PLACEMENTS'
        landing_page_view = 'LANDING_PAGE_VIEW'
        landing_page_view_optimization_goal = 'LANDING_PAGE_VIEW_OPTIMIZATION_GOAL'
        landing_page_view_precreate = 'LANDING_PAGE_VIEW_PRECREATE'
        lead_ads_guidance = 'LEAD_ADS_GUIDANCE'
        learning_limited = 'LEARNING_LIMITED'
        learning_pause_friction = 'LEARNING_PAUSE_FRICTION'
        learning_phase_budget_edits = 'LEARNING_PHASE_BUDGET_EDITS'
        low_budget_utilization = 'LOW_BUDGET_UTILIZATION'
        low_outcome = 'LOW_OUTCOME'
        merlin_guidance = 'MERLIN_GUIDANCE'
        messaging_events = 'MESSAGING_EVENTS'
        messaging_events_precreate = 'MESSAGING_EVENTS_PRECREATE'
        messaging_partners = 'MESSAGING_PARTNERS'
        messaging_partners_precreate = 'MESSAGING_PARTNERS_PRECREATE'
        meta_verified_ads_performance_guidance = 'META_VERIFIED_ADS_PERFORMANCE_GUIDANCE'
        missing_or_invalid_parameters = 'MISSING_OR_INVALID_PARAMETERS'
        mixed_formats = 'MIXED_FORMATS'
        mixed_pa_combine_adsets = 'MIXED_PA_COMBINE_ADSETS'
        mmt_carousel_to_video = 'MMT_CAROUSEL_TO_VIDEO'
        mobile_first_creative = 'MOBILE_FIRST_CREATIVE'
        mobile_first_video = 'MOBILE_FIRST_VIDEO'
        mr_aemv2sub_kconsolidation = 'MR_AEMV2SUB_KCONSOLIDATION'
        multi_advertiser_ads = 'MULTI_ADVERTISER_ADS'
        multi_text = 'MULTI_TEXT'
        music = 'MUSIC'
        not_applicable = 'NOT_APPLICABLE'
        no_delivery_status = 'NO_DELIVERY_STATUS'
        offsite_conversion = 'OFFSITE_CONVERSION'
        optimal_bau = 'OPTIMAL_BAU'
        outcome_forecaster_shadow_logging = 'OUTCOME_FORECASTER_SHADOW_LOGGING'
        payment_method = 'PAYMENT_METHOD'
        performant_creative_reels_opt_in = 'PERFORMANT_CREATIVE_REELS_OPT_IN'
        pfr_l1_inline_mmt = 'PFR_L1_INLINE_MMT'
        pixel_optimization_aam = 'PIXEL_OPTIMIZATION_AAM'
        pixel_optimization_aam_precreate = 'PIXEL_OPTIMIZATION_AAM_PRECREATE'
        pixel_optimization_hie = 'PIXEL_OPTIMIZATION_HIE'
        pixel_optimization_hie_precreate = 'PIXEL_OPTIMIZATION_HIE_PRECREATE'
        pixel_setup = 'PIXEL_SETUP'
        pixel_setup_precreate = 'PIXEL_SETUP_PRECREATE'
        pixel_upsell = 'PIXEL_UPSELL'
        placements_liquidity_automatic_guidance = 'PLACEMENTS_LIQUIDITY_AUTOMATIC_GUIDANCE'
        predictive_creative_limited = 'PREDICTIVE_CREATIVE_LIMITED'
        predictive_creative_limited_hourly = 'PREDICTIVE_CREATIVE_LIMITED_HOURLY'
        preparing_status = 'PREPARING_STATUS'
        purchase_optimization = 'PURCHASE_OPTIMIZATION'
        rapid_learning_limited = 'RAPID_LEARNING_LIMITED'
        rapid_learning_phase = 'RAPID_LEARNING_PHASE'
        reach_optimization_goal = 'REACH_OPTIMIZATION_GOAL'
        reach_optimization_goal_precreate = 'REACH_OPTIMIZATION_GOAL_PRECREATE'
        reels_duplication_upsell = 'REELS_DUPLICATION_UPSELL'
        reels_music_duplication = 'REELS_MUSIC_DUPLICATION'
        reels_pc_and_mobile_first_creative = 'REELS_PC_AND_MOBILE_FIRST_CREATIVE'
        reels_performant_creative = 'REELS_PERFORMANT_CREATIVE'
        reels_placement = 'REELS_PLACEMENT'
        revert = 'REVERT'
        sabr_default_duration = 'SABR_DEFAULT_DURATION'
        sales_conversion = 'SALES_CONVERSION'
        scale_good_campaign = 'SCALE_GOOD_CAMPAIGN'
        scale_good_campaign_duplication = 'SCALE_GOOD_CAMPAIGN_DUPLICATION'
        scale_good_campaign_smb = 'SCALE_GOOD_CAMPAIGN_SMB'
        scale_good_ctx_campaign = 'SCALE_GOOD_CTX_CAMPAIGN'
        semantic_based_audience_duplication = 'SEMANTIC_BASED_AUDIENCE_DUPLICATION'
        semantic_based_audience_expansion = 'SEMANTIC_BASED_AUDIENCE_EXPANSION'
        setup_pixel = 'SETUP_PIXEL'
        shops_ads = 'SHOPS_ADS'
        shops_ads_duplication = 'SHOPS_ADS_DUPLICATION'
        shops_ads_traffic_cap_settings = 'SHOPS_ADS_TRAFFIC_CAP_SETTINGS'
        shop_ads_v2 = 'SHOP_ADS_V2'
        signals_growth_capi = 'SIGNALS_GROWTH_CAPI'
        signals_growth_capi_precreate = 'SIGNALS_GROWTH_CAPI_PRECREATE'
        signals_growth_capi_table = 'SIGNALS_GROWTH_CAPI_TABLE'
        signals_growth_capi_v2 = 'SIGNALS_GROWTH_CAPI_V2'
        similar_advertiser_budget_recommendation = 'SIMILAR_ADVERTISER_BUDGET_RECOMMENDATION'
        site_extensions_duplication = 'SITE_EXTENSIONS_DUPLICATION'
        six_plus_manual_placements = 'SIX_PLUS_MANUAL_PLACEMENTS'
        six_plus_placements_duplication = 'SIX_PLUS_PLACEMENTS_DUPLICATION'
        spend_limit = 'SPEND_LIMIT'
        syd_test_mode = 'SYD_TEST_MODE'
        tailored_lead_ad_campaign = 'TAILORED_LEAD_AD_CAMPAIGN'
        tailored_messages_campaign = 'TAILORED_MESSAGES_CAMPAIGN'
        tla_creation_package = 'TLA_CREATION_PACKAGE'
        top_adsets_with_ads_under_cap = 'TOP_ADSETS_WITH_ADS_UNDER_CAP'
        top_campaigns_with_ads_under_cap = 'TOP_CAMPAIGNS_WITH_ADS_UNDER_CAP'
        two_p_guidance_card_aaa = 'TWO_P_GUIDANCE_CARD_AAA'
        two_p_guidance_card_auto_placement = 'TWO_P_GUIDANCE_CARD_AUTO_PLACEMENT'
        two_p_guidance_card_cbo_off = 'TWO_P_GUIDANCE_CARD_CBO_OFF'
        two_p_guidance_card_ctm_preflight = 'TWO_P_GUIDANCE_CARD_CTM_PREFLIGHT'
        uncrop_image = 'UNCROP_IMAGE'
        uneconomical_ads_throttling = 'UNECONOMICAL_ADS_THROTTLING'
        unified_inbox = 'UNIFIED_INBOX'
        unused_budget = 'UNUSED_BUDGET'
        value_diagnostics_guidance = 'VALUE_DIAGNOSTICS_GUIDANCE'
        video_length = 'VIDEO_LENGTH'
        video_views_upsell = 'VIDEO_VIEWS_UPSELL'
        video_views_upsell_precreate = 'VIDEO_VIEWS_UPSELL_PRECREATE'
        wa_messaging_partners = 'WA_MESSAGING_PARTNERS'
        wa_messaging_partners_precreate = 'WA_MESSAGING_PARTNERS_PRECREATE'
        web_engaged_view_conversions = 'WEB_ENGAGED_VIEW_CONVERSIONS'
        zero_conversion = 'ZERO_CONVERSION'
        zero_impression = 'ZERO_IMPRESSION'

    _field_types = {
        'actor_id': 'string',
        'actor_name': 'string',
        'ad_limit_scope_business': 'Business',
        'ad_limit_scope_business_manager_id': 'string',
        'ad_limit_set_by_page_admin': 'unsigned int',
        'ads_running_or_in_review_count': 'unsigned int',
        'ads_running_or_in_review_count_subject_to_limit_set_by_page': 'unsigned int',
        'current_account_ads_running_or_in_review_count': 'unsigned int',
        'future_limit_activation_date': 'string',
        'future_limit_on_ads_running_or_in_review': 'unsigned int',
        'limit_on_ads_running_or_in_review': 'unsigned int',
        'recommendations': 'list<Object>',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['RecommendationType'] = AdAccountAdVolume.RecommendationType.__dict__.values()
        return field_enum_info


