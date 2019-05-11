<?php

namespace MountainTales\Packing\Model;

use Magento\Framework\Model\AbstractModel;
use MountainTales\Packing\Model\ResourceModel\[resource_model] as [resource_model]Resource;

/**
 * Class [model]
 *
 * @package   MountainTales\Packing\Model
 * @author    Jaep Cuperus <jaep@mountain-it.nl>
 * @copyright 24-4-19
 * @license   https://www.mountain-it.nl Commercial License
 */
class [model] extends AbstractModel
{
    /**
     * [model] constructor
     */
    protected function _construct()
    {
        $this->_init([resource_model]Resource::class);
    }
}